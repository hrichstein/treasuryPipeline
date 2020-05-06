def check_directories():
    """
    Checks for and creates the directories and subdirectories that will be used throughout the rest of
    the code.

    -This will also remove the files that are not necessary to run HPU_Reduce if they still exist.
     This includes the README.md file, so you will want to view this on the github page as it will be
     easier to see anyway.  If you would like to modify the file structure, you can do so here.

    -This also assumes you have cloned the github repository into the directory that you wish to
     run everything in.  If you accidentally clone it somewhere else, you can move the files
     and directories or add an additional path to where the data are.
    -----------------------------------------------------------------------------------------------------
    Takes in:
        Nothin
    -----------------------------------------------------------------------------------------------------
    Creates the following directories:
         ⃝ raw_frames
         ⃝ cal_frames
            - bias_frames
            - dark_frames
            - flat_frames
         ⃝ red_frames
         ⃝ file_outputs
            -logs
            -data_sheets
         ⃝ plots
    -----------------------------------------------------------------------------------------------------
    Removes the following files if they exist:
         ⃝ logo.png
         ⃝ file_tree.png
         ⃝ README.md
         ⃝ LICENSE
    -----------------------------------------------------------------------------------------------------
    Outputs:
        A dictionary containing all of the directories and their respective paths
    -----------------------------------------------------------------------------------------------------
    """
    # ------------------------  Remove specified files  ------------------------ #
    rm_files = ["logo.png","file_tree.png","README.md","LICENSE"]

    for file in rm_files:
        if(os.path.exists(file)==True):
            os.remove(file)

    # ------------------------  Create specified directories  ------------------------ #
    int_dirs = ["raw_frames","cal_frames","red_frames","file_outputs","plots"]
    cal_dirs = ["bias_frames","dark_frames","flat_frames"]
    out_dirs = ["logs","data_sheets"]

    all_dirs = int_dirs+cal_dirs+out_dirs
    all_paths = []

    for int_dir in int_dirs:
        if not os.path.exists(os.path.join(".",int_dir)):
            os.makedirs(int_dir)
        all_paths.append(os.path.join(".",int_dir))
    for cal_dir in cal_dirs:
        if not os.path.exists(os.path.join(".","cal_frames",cal_dir)):
            os.makedirs(os.path.join(".","cal_frames",cal_dir))
        all_paths.append(os.path.join(".","cal_frames",cal_dir))
    for out_dir in out_dirs:
        if not os.path.exists(os.path.join(".","file_outputs",out_dir)):
            os.makedirs(os.path.join(".","file_outputs",out_dir))
        all_paths.append(os.path.join(".","file_outputs",out_dir))

    return dict(zip(all_dirs,all_paths))
