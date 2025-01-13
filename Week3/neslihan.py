# List Tasks
def list_tasks(tasks, status=["Pending", "Completed"]):
    """
    Lists all tasks with their status in a grid format.
    """
    filtered_tasks = [task for task in tasks if task["status"] in status]
    
    #1 Print grid header
    print(f"\n{'ID':<5}{'Name':<30}{'Status':<15}")
   
    print("-" * 50)
    * 50: Tire karakterini 50 defa tekrarlayarak bir çizgi oluşturur.


    for task_id in sorted([task["id"] for task in filtered_tasks]):
        for task in filtered_tasks:
            if task["id"] == task_id:
                print(f"{task['id']:<5}{task['name']:<30}{task['status']:<15}")
                break

#print_grid(None, filtered_tasks)
    task_count = len(filtered_tasks)
    print(f"\n Total tasks listed: {task_count}")

    return task_count
