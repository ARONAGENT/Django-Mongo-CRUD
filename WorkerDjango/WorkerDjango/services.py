import pymongo
from pymongo import MongoClient
class WorkersOperation:
    def insertWorker(self,dic):
        try:
            client=MongoClient("mongodb+srv://rohan2024:Aronagent2024@aroncluster.69g2e.mongodb.net/?retryWrites=true&w=majority&appName=AronCluster")
            db=client['arondb']
            coll=db['workers']
            coll.insert_one(dic)
            client.close()
            stat='Successful'
        except:
            stat='Failed .....'
        return {'status':stat}
    
    def listworkers(self):
        try:
            client=MongoClient("mongodb+srv://rohan2024:Aronagent2024@aroncluster.69g2e.mongodb.net/?retryWrites=true&w=majority&appName=AronCluster")
            db=client['arondb']
            coll=db['workers']
            workers = [] 
            for data in coll.find():
                workers.append(data)
            client.close()
            stat='Worker list retreive Successfully'
        except:
            stat='Failed .....'
        return {'values':workers,'status':stat}
    
    def incrementsal(self,dic):
        try:
            client=MongoClient("mongodb+srv://rohan2024:Aronagent2024@aroncluster.69g2e.mongodb.net/?retryWrites=true&w=majority&appName=AronCluster")
            db=client['arondb']
            coll=db['workers']
            wid={'workerId':dic['workerId']}
            condition={'$inc':{'salary':dic['salary']}}
            print(wid)
            print(condition)
            res=coll.update_one(wid,condition)
            if res.matched_count>0:
                stat='Worker  Salary increment Successfully'
            else:
                stat='failed'
            client.close()
        except:
            stat='Failed .....'
        return {'status':stat}

    def deleteWorker(self,dic):
        try:
            client=MongoClient("mongodb+srv://rohan2024:Aronagent2024@aroncluster.69g2e.mongodb.net/?retryWrites=true&w=majority&appName=AronCluster")
            db=client['arondb']
            coll=db['workers']
            wid={'workerId':dic['workerId']}
            res=coll.delete_one(wid)
            if res.deleted_count>0:
                stat='Worker deleted Successfully'
            else:
                stat='Failed to Delete'
            client.close()
        except:
            stat='Failed .....'
        return {'status':stat}
