from classes import TaskInventory

def test_class_inventory():
    
    assert TaskInventory
    
    test_task_inv = TaskInventory()
    assert isinstance(test_task_inv, CarInventory)
    assert isinstance(test_task_inv.tasks, list)