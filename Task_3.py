def hanoi_tower(n, source, target, auxiliary, state):
    if n > 0:
        # Перемістити n-1 дисків з source на auxiliary, використовуючи target як допоміжний
        hanoi_tower(n-1, source, auxiliary, target, state)
        
        # Перемістити останній диск з source на target
        disk = state[source].pop()
        state[target].append(disk)
        print(f"Перемістити диск з {source} на {target}: {disk}")
        print(f"Проміжний стан: {state}")
        
        # Перемістити n-1 дисків з auxiliary на target, використовуючи source як допоміжний
        hanoi_tower(n-1, auxiliary, target, source, state)

def main():
    n = int(input("Введіть кількість дисків: "))
    
    # Початковий стан стрижнів
    state = {
        'A': list(range(n, 0, -1)), 
        'B': [],
        'C': []
    }
    
    print(f"Початковий стан: {state}")
    
    # Викликаємо функцію для переміщення всіх дисків зі стрижня A на C
    hanoi_tower(n, 'A', 'C', 'B', state)
    
    print(f"Кінцевий стан: {state}")

if __name__ == "__main__":
    main()
