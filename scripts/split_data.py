import os
import shutil

# a simple data spliter to shrink our dataset.

def select(mydir, ratio = 0.5):
    if not os.path.exists(mydir+"_backup"):
        os.mkdir(mydir+"_backup")
    else:
        shutil.rmtree(mydir+"_backup")
        os.mkdir(mydir+"_backup")

    print(mydir+"_backup")
    img_dir = os.listdir(mydir)
    img_dir.sort()
    print(mydir + " length: ",len(img_dir))
    for index, file in enumerate(img_dir):
        if index > int(len(img_dir)* ratio):
            if file[:4] != img_dir[int(len(img_dir)*ratio)][:4]:
#                 os.remove?~Hos.path.join(mydir,file)?~I
                shutil.copy(os.path.join(mydir,file),mydir+"_backup")
                print(index, ":" + os.path.join(mydir,file))

root = "/home/yl58n21/MMT/examples/data"       # adjust your root dir
dir1 = "dukemtmc/DukeMTMC-reID"
dir2 = "market1501/Market-1501-v15.09.15"

duke_bbx_train = os.path.join(root, dir1,"bounding_box_train")
duke_bbx_test =  os.path.join(root, dir1,"bounding_box_test")
market_bbx_train = os.path.join(root,dir2,"bounding_box_train")
market_bbx_test = os.path.join(root, dir2,"bounding_box_test")


select(duke_bbx_train,0.5)
select(duke_bbx_test,0.5)
select(market_bbx_train,0.5)
select(market_bbx_test,0.5)

os.rename(duke_bbx_train,duke_bbx_train+"_origin")
os.rename(duke_bbx_test,duke_bbx_test+"_origin")
os.rename(market_bbx_train,market_bbx_train+"_origin")
os.rename(market_bbx_test,market_bbx_test+"_origin")
os.rename(duke_bbx_train+"_backup",duke_bbx_train)
os.rename(duke_bbx_test+"_backup",duke_bbx_test)
os.rename(market_bbx_train+"_backup",market_bbx_train)
os.rename(market_bbx_test+"_backup",market_bbx_test)