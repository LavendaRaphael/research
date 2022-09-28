from dpdispatcher import Machine, Resources, Task, Submission
import copy

machine = Machine.load_from_json('machine.json')
resources = Resources.load_from_json('resources.json')

task = Task.load_from_json('task.json')
dir_list = [
    'H2CO3_TT_H2O_126',
    'H2CO3_CC_H2O_126',
    'H2CO3_CT_H2O_126'
]

task_list = []
for str_dir in dir_list:
    task_tmp = copy.copy(task)
    task_tmp.task_work_path = str_dir
    task_list.append( task_tmp )


submission = Submission(work_base='../',
    machine=machine, 
    resources=resources,
    task_list=task_list,
    forward_common_files=[
        "frozen_model.pb",
        "input.lammps"
    ], 
    backward_common_files=[]
)
submission.run_submission()
