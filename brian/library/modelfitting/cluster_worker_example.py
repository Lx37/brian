from cluster_modelfitting_fast import *
#from cluster_modelfitting import *

if __name__=='__main__':
    cluster_worker_script(light_worker,
                          named_pipe=True)
    