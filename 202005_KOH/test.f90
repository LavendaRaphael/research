program main
implicit none

real :: a(2)

a=[ 1.0, 9.0 ]
a=a/sum(a)
print *,a

end
