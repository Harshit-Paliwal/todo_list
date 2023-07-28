class tasks ():
    def __init__(self,mongo_db_collection_object) -> None:
        self.db = mongo_db_collection_object
        
    def add_task(self,task_no,task_name,task_brief):
        if self.db.count_documents({"task_no":task_no})>0:
            return False
        doc = {
            "task_no":task_no,
            "task_name":task_name,
            "task_brief":task_brief
        }
        self.db.insert_one(doc)
        return True
    