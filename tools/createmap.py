import os,sys



if __name__=="__main__":
    path=sys.argv[1]
    path_to_mojomap="."
    if not os.path.exists(path):
        os.mkdir(path)
    os.system("cp -arv %s %s/mojomaps" %(os.path.join(path_to_mojomap,"web"),path))
    