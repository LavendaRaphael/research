/* +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
   Copyright (c) 2011-2016 The plumed team
   (see the PEOPLE file at the root of the distribution for a list of names)

   See http://www.plumed.org for more information.

   This file is part of plumed, version 2.

   plumed is free software: you can redistribute it and/or modify
   it under the terms of the GNU Lesser General Public License as published by
   the Free Software Foundation, either version 3 of the License, or
   (at your option) any later version.

   plumed is distributed in the hope that it will be useful,
   but WITHOUT ANY WARRANTY; without even the implied warranty of
   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
   GNU Lesser General Public License for more details.

   You should have received a copy of the GNU Lesser General Public License
   along with plumed.  If not, see <http://www.gnu.org/licenses/>.
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ */
#include "vatom/ActionWithVirtualAtom.h"
#include "vatom/ActionRegister.h"
#include "core/PlumedMain.h"
#include "core/Atoms.h"

#include "tools/Pbc.h"
#include <string>
#include <cmath>

#include <iostream>
#include <iomanip>  // needed to use manipulators with parameters (precision, width)
#include <fstream>

using namespace std;

namespace PLMD{
namespace vatom{

//+PLUMEDOC VATOM CENTER
/*
Calculate the position of the PROTON CV 

The computed
virtual atom is a proton tracker and be accessed in
an atom list through the label for the PROTON action that creates it.

When running with periodic boundary conditions, it uses the inbuilt plumed PBC




\par Examples

# definition of CVs

c1: PROTON ALLATOMS=1-192 NN=14 MM=28 GAMMA=14 NO=64 NH=128 R_0=1.30 OFFSET_DEFAULT=1.8 OFFSET_INDEX=1,2 OFFSET_VALUE=0,0
DUMPATOMS STRIDE=10 FILE=proton.xyz ATOMS=c1

distance: DISTANCE ATOMS=c1,2


# lets move the proton from (almost) 1 to 3 Angstrom in 2000 steps and then keep it there for another 1000 steps 
MOVINGRESTRAINT ...
 LABEL=steer
 ARG=distance
 STEP0=0  AT0=1.0  KAPPA0=5.0
 STEP1=2000  AT1=3.0  KAPPA1=10.0
 STEP2=3000  AT2=3.0  KAPPA2=10.0
... MOVINGRESTRAINT


PRINT ARG=distance,steer.distance_cntr,steer.bias,steer.force2 STRIDE=1  FILE=colvar.out


\verbatim
\endverbatim
(See also \ref DISTANCE, \ref MOVINGRESTRAINT and \ref PRINT).

*/
//+ENDPLUMEDOC


class Proton:
  public ActionWithVirtualAtom
{
  std::vector<double> coordnums, weight, offset, offsetvalue;
  std::vector<int> offsetindex;
  std::vector< std::vector<Vector> > derivcn;
  std::vector< std::vector<double> > derivw;
  std::vector<Vector> distref;

  int no,nh,nn,mm,j;
  double r0,gamma,offsetdefault;
  bool pbc,forcebubble;
public:
  explicit Proton(const ActionOptions&ao);
  void calculate();
  static void registerKeywords( Keywords& keys );
};

PLUMED_REGISTER_ACTION(Proton,"PROTON")

void Proton::registerKeywords(Keywords& keys){
  ActionWithVirtualAtom::registerKeywords(keys);
  keys.add("compulsory","NN","6","The n parameter of the switching function ");
  keys.add("compulsory","MM","0","The m parameter of the switching function; 0 implies 2*NN");
  keys.add("compulsory","OFFSET_DEFAULT","2","The default offset parameter of the weight function ");
  keys.add("compulsory","GAMMA","8","The gamma parameter of the weight function. ");
  keys.add("compulsory","NO","64","The number of oxygen atoms ");
  keys.add("compulsory","NH","128","The number of hydrogen atoms.");
  keys.add("compulsory","R_0","The r_0 parameter of the switching function");
  keys.addFlag("NOPBC",false,"ignore the periodic boundary conditions when calculating distances");
  keys.addFlag("FORCEBUBBLE",false,"ignore the artificial force bubble around imax");
  keys.addFlag("MASS",false,"If set center is mass weighted");
  keys.add("allatoms","ALLATOMS","Calculate the distances between all the atoms in GROUPA and all "
                              "the atoms in GROUPB. This must be used in conjuction with GROUPB.");
  keys.add("optional","OFFSET_INDEX","Index of individual oxygen atoms for which offsets will be defined"); 
  keys.add("optional","OFFSET_VALUE","Individual offsets in the same order as the index above"); 
}

Proton::Proton(const ActionOptions&ao):
  Action(ao),
  ActionWithVirtualAtom(ao),
  pbc(true),
  forcebubble(false)
{

 
  vector<AtomNumber> allatoms;
  parseAtomList("ALLATOMS",allatoms);
  
    parse("R_0",r0);
    if(r0<=0.0) error("R_0 should be explicitly specified and positive");
    

    parse("NN",nn);
    parse("MM",mm);
    parse("NO",no);
    parse("NH",nh);
    parse("GAMMA",gamma);
    parse("OFFSET_DEFAULT",offsetdefault);
    parseVector("OFFSET_INDEX",offsetindex); 
    parseVector("OFFSET_VALUE",offsetvalue); 
  
  bool nopbc=!pbc;
  parseFlag("NOPBC",nopbc);
  parseFlag("FORCEBUBBLE",forcebubble);
  pbc=!nopbc;
  checkRead();
  Vector zero;

  log.printf("  of group of atoms");
  for(unsigned i=0;i<allatoms.size();++i) log.printf(" %d",allatoms[i].serial());
  log.printf("  \n");

    derivcn.resize(no);
    for(unsigned i=0;i<no;i++) derivcn[i].resize(no+nh);

    derivw.resize(no);
    for(unsigned i=0;i<no;i++) derivw[i].resize(no);

    distref.resize(no);
    coordnums.resize(no);
    weight.resize(no);
    offset.resize(no);



  if( offsetvalue.size()!=offsetindex.size() ) error("number of elements in OFFSET_VALUE vector does not match the number of OFFSET_INDEX");
  for(unsigned i=0;i<no;i++) offset[i] = offsetdefault;
  for(unsigned i=0;i<offsetvalue.size();i++){
    j = offsetindex[i]-1;
    offset[j] = offsetvalue[i];
  }
  for(unsigned i=0;i<offset.size();++i) log.printf("for atom index %d the offset is %f \n",allatoms[i].serial(),offset[i]);
  log.printf("\n");
 

  if(pbc) log.printf("  using periodic boundary conditions\n");
  else    log.printf("  without periodic boundary conditions\n");

  if(nopbc){
    log<<"  PBC will be ignored\n";
  } else {
    log<<"  broken molecules will be rebuilt assuming atoms are in the proper order\n";
  }
    
  if(forcebubble) log.printf(" Forces will be around 3 Ang of imax \n");

  log.printf("  number of H-acceptors: %d\n",no); 
  log.printf("  number of hydrogens  : %d\n",nh); 
  log.printf("  coord.num. r0        : %lf\n",r0); 
  log.printf("  coord.num. nn        : %d\n",nn); 
  log.printf("  coord.num. mm        : %d\n",mm); 
  log.printf("  weighting gamma      : %lf\n",gamma); 
  requestAtoms(allatoms);
}


void Proton::calculate(){

  Vector pos,temp,poscheck,zero;
  vector<Tensor> deriv(getNumberOfAtoms());
  vector<Tensor> derivcheck(getNumberOfAtoms());
  int io, i;
  double dr=0.0, sum=0.0;
  int imax=0;
  double max=0.0,dfunc=0.0;
  double invr0=1.0/r0; 


  /* initialize things to zero */
  for(unsigned i=0;i<getNumberOfAtoms();i++){
    for(unsigned k=0;k<3;k++){
      deriv[i][k][k]=0.0;
      derivcheck[i][k][k]=0.0;
    }
  } 

  for(unsigned j=0;j<3;j++) zero[j] = 0.0;
  for(unsigned i=0;i<no;i++){
    distref[i] = zero;
    coordnums[i] = 0.0;
    weight[i] = 0.0;
    for(unsigned j=0;j<no+nh;j++){
      for(unsigned k=0;k<3;k++){
        derivcn[i][j][k] = 0.0;
      }
    }
    for(unsigned j=0;j<no;j++){
      derivw[i][j] = 0.0;
    }
  }


  /* Calculating coordination number for each oxygen atoms */
  /*   cn(r) = (1-(r/r0)**nn) / (1-(r/r0)**mm)              */


  for(unsigned io=0;io<no;io++){
    coordnums[io]=0.0;
    for(unsigned ih=no;ih<nh+no;ih++){
      
      Vector distance = pbcDistance(getPosition(io), getPosition(ih));
      dr = distance.modulo();
      const double rdist = dr * invr0;
      double rNdist=Tools::fastpow(rdist,nn-1);
      double rMdist=Tools::fastpow(rdist,mm-1);
      double num = 1.0-rNdist*rdist;
      double iden = 1.0/(1.0-rMdist*rdist);
      double func = num*iden;
      
      coordnums[io] += func;
      dfunc = ((-nn*rNdist*iden)+(func*(iden*mm)*rMdist));
      dfunc*=invr0;
      dfunc/=dr;
      Vector dd(dfunc*distance);
      derivcn[io][ih] = dd;
      derivcn[io][io] -= dd;
    }
  }
  

  /* weight associated with each oxygen atom */
  sum=0.0;
  for(unsigned iat=0;iat<no;iat++){
    weight[iat] = exp( gamma * (coordnums[iat] - offset[iat]) );
    sum += weight[iat];
  }
  for(unsigned iat=0;iat<no;iat++) weight[iat] /= sum;
  
  /* find oxygen with highest coordination number */
  max=-999.9;
  for(unsigned i=0;i<no;i++){
    if(weight[i]>max){
      imax=i;
      max=weight[i];
    }
  }
  

  /* make force bubble around imax by setting weights outside to zero */
  if(forcebubble){
    sum=0.0;
    for(unsigned iat=0;iat<no;iat++){
      Vector disderiv = pbcDistance(getPosition(imax), getPosition(iat));
      dr = disderiv.modulo();
      if(dr<3.0){
	weight[iat] = exp( gamma * (coordnums[iat] - offset[iat]) );
	sum += weight[iat];
      }else{
	weight[iat]=0.0;
      }
    }
    for(unsigned iat=0;iat<no;iat++) weight[iat] /= sum;
  }  


  /* derivatives of weight with respect to coordination number */
  for(unsigned i=0;i<no;i++){
    for(unsigned j=0;j<no;j++){
      if(j!=i){
        derivw[i][j] = -1.0*weight[i]*gamma*weight[j];
      }
    }
    derivw[i][i] = gamma*weight[i]*(1.0-weight[i]);
  }


  /* sum weighted distances from reference oxygen */
  pos=getPosition(imax);
  for(unsigned i=0;i<no;i++){
    distref[i] = pbcDistance(getPosition(imax), getPosition(i));
    pos += distref[i] * weight[i];
  }
  
  /* Calculating derivatives */
  for(unsigned i=0;i<getNumberOfAtoms();i++){
     for(unsigned j=0;j<no;j++){
        for(unsigned l=0;l<no;l++){
           for(unsigned k=0;k<3;k++){
	     for(unsigned m=0;m<3;m++) deriv[i][k][m]+=distref[j][m]*derivw[j][l]*derivcn[l][i][k];
           }
        }
     }
   }
  
  for(unsigned k=0;k<3;k++) deriv[imax][k][k]+=1.0;

  for(unsigned j=0;j<no;j++){
     if(j!=imax){ 
       for(unsigned k=0;k<3;k++){
          deriv[j][k][k]+=weight[j];
          deriv[imax][k][k]-=weight[j];
       }
     }
  } 


  /* set final positions and derivatives */
  setPosition(pos);
  //  setMass(mass);
  setAtomsDerivatives(deriv); 

  
}   /* for calculate */ 
}   /* for namespace vatom */
}   /* for namespace PLMD */
