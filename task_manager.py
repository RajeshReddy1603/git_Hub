import json
import datetime
from typing import List, Dict, Optional

class Task:
    def __init__(self, title: str, description: str = "", priority: str = "medium"):
        self.id = hash(title + str(datetime.datetime.now()))
        self.title = title
        self.description = description
        self.priority = priority
        self.completed = False
        self.created_at = datetime.datetime.now().isoformat()
    
    def to_dict(self) -> Dict:
        return {
            'id': self.id,
            'title': self.title,
            'description': self.description,
            'priority': self.priority,
            'completed': self.completed,
            'created_at': self.created_at
        }
    
    @classmethod
    def from_dict(cls, data: Dict):
        task = cls(data['title'], data['description'], data['priority'])
        task.id = data['id']
        task.completed = data['completed']
        task.created_at = data['created_at']
        return task

class TaskManager:
    def __init__(self, filename: str = "tasks.json"):
        self.filename = filename
        self.tasks: List[Task] = []
        self.load_tasks()
    
    def add_task(self, title: str, description: str = "", priority: str = "medium") -> Task:
        task = Task(title, description, priority)
        self.tasks.append(task)
        self.save_tasks()
        return task
    
    def complete_task(self, task_id: int) -> bool:
        for task in self.tasks:
            if task.id == task_id:
                task.completed = True
                self.save_tasks()
                return True
        return False
    
    def delete_task(self, task_id: int) -> bool:
        for i, task in enumerate(self.tasks):
            if task.id == task_id:
                del self.tasks[i]
                self.save_tasks()
                return True
        return False
    
    def get_tasks(self, completed: Optional[bool] = None) -> List[Task]:
        if completed is None:
            return self.tasks
        return [task for task in self.tasks if task.completed == completed]
    
    def get_tasks_by_priority(self, priority: str) -> List[Task]:
        return [task for task in self.tasks if task.priority == priority]
    
    def save_tasks(self):
        try:
            with open(self.filename, 'w') as f:
                json.dump([task.to_dict() for task in self.tasks], f, indent=2)
        except Exception as e:
            print(f"Error saving tasks: {e}")
    
    def load_tasks(self):
        try:
            with open(self.filename, 'r') as f:
                data = json.load(f)
                self.tasks = [Task.from_dict(task_data) for task_data in data]
        except FileNotFoundError:
            self.tasks = []
        except Exception as e:
            print(f"Error loading tasks: {e}")
            self.tasks = []

def main():
    tm = TaskManager()
    
    while True:
        print("\n=== Task Manager ===")
        print("1. Add task")
        print("2. View all tasks")
        print("3. View pending tasks")
        print("4. Complete task")
        print("5. Delete task")
        print("6. View by priority")
        print("7. Exit")
        
        choice = input("\nEnter choice (1-7): ").strip()
        
        if choice == '1':
            title = input("Task title: ")
            desc = input("Description (optional): ")
            priority = input("Priority (low/medium/high): ") or "medium"
            task = tm.add_task(title, desc, priority)
            print(f"Added task: {task.title}")
        
        elif choice == '2':
            tasks = tm.get_tasks()
            if not tasks:
                print("No tasks found.")
            else:
                for task in tasks:
                    status = "✓" if task.completed else "○"
                    print(f"{status} [{task.priority}] {task.title} (ID: {task.id})")
        
        elif choice == '3':
            tasks = tm.get_tasks(completed=False)
            if not tasks:
                print("No pending tasks.")
            else:
                for task in tasks:
                    print(f"○ [{task.priority}] {task.title} (ID: {task.id})")
        
        elif choice == '4':
            try:
                task_id = int(input("Enter task ID to complete: "))
                if tm.complete_task(task_id):
                    print("Task completed!")
                else:
                    print("Task not found.")
            except ValueError:
                print("Invalid ID.")
        
        elif choice == '5':
            try:
                task_id = int(input("Enter task ID to delete: "))
                if tm.delete_task(task_id):
                    print("Task deleted!")
                else:
                    print("Task not found.")
            except ValueError:
                print("Invalid ID.")
        
        elif choice == '6':
            priority = input("Enter priority (low/medium/high): ")
            tasks = tm.get_tasks_by_priority(priority)
            if not tasks:
                print(f"No {priority} priority tasks found.")
            else:
                for task in tasks:
                    status = "✓" if task.completed else "○"
                    print(f"{status} {task.title} (ID: {task.id})")
        
        elif choice == '7':
            print("Goodbye!")
            break
        
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()