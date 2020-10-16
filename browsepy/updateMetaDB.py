import pycountry
import os
import datetime
from . import db, models
from sys import argv

def get_dir_size(start_path):
    total_size = 0
    for dirpath, dirnames, filenames in os.walk(start_path):
        for f in filenames:
            p = os.path.join(dirpath, f)
            size = os.path.getsize(p)
            total_size += size
    return total_size

def add_path_to_db(path, size):
    try:
        meta = models.Metadata.query.filter_by(path=path).one()
    except:
        meta = models.Metadata()
        meta.path = path
    finally:
        meta.size = size
        meta.size_date = datetime.datetime.now()
        db.session.add(meta)
        db.session.commit()

def update_db(path):
    add_path_to_db(path,get_dir_size(path))
    for root, dirs, files in os.walk(path):
        for dir in dirs:
            path = os.path.join(root,dir)
            size = get_dir_size(path)
            add_path_to_db(path,size)
        for name in files:
            path = os.path.join(root,name)
            size = os.path.getsize(path)
            add_path_to_db(path,size)
            

def add_descriptions():

    for root, dirs, files in os.walk(dirname):
        for d in dirs:
            if "UNISDR/Hazard/Flood scenarios" in d:
                for filename in os.listdir(d):
                    meta = models.Metadata.query.filter_by(path=os.path.join(dirname, filename)).one()
                    meta.desc = pycountry.countries.get(alpha_2=filename.split('.')[0]).name
                    db.session.commit()
            if "UNISDR/Exposure" in d:
                for name in os.listdir(d):
                    path = (os.path.join(root, name))
                    countrycode = path.split('_')[1].split('.')[0]
                    desc = pycountry.countries.get(alpha_3=countrycode.upper()).name
                    try:
                        meta = models.Metadata.query.filter_by(path=path).one()
                        meta.desc = desc
                        db.session.commit()
                    except:
                        meta = models.Metadata()
                        meta.path = path
                        meta.desc = desc
                        db.session.add(meta)
                        db.session.commit()

        for name in files:
            path = (os.path.join(root, name))
            try:
                meta = models.Metadata.query.filter_by(path=path).one()
            except:
                meta = models.Metadata()
                meta.path = path
                meta.desc = desc
                db.session.add(meta)
                db.session.commit()
