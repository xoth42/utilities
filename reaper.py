#!/usr/bin/python3

if __name__ =="__main__":
    """
    Kills defunct processes
    xoth42 11/20/2022
    """
    from proc.core import find_processes
    from proc.unix import UnixProcess
    all_procs = find_processes()
    z_procs = []
    print("Reaper - kill all zombie processes\n")
    for process in all_procs:
        if process.state == "Z":
            z_procs.append(process)
            print(process.exe_name, process.pid)

    print("Found",len(z_procs), "zombie processes")
    if len(z_procs) > 0:
        user_in = str(input("Do you want to kill all of them?\n(nothing or y/yes, otherwise anything)\n")).lower()
    else:
        print("\n")
        exit(0)
    if user_in == "" or user_in == "y" or user_in == "yes":
        for process in z_procs:
            np = UnixProcess(pid = process.pid)
            np.kill_helper()
        print("Done\n")
    else:
        print ("\n")


