import turtle

def draw_koch_segment(t, length, level):
    """Рекурсивно малює одну сторону сніжинки Коха."""
    if level == 0:
        t.forward(length)
    else:
        length /= 3.0
        draw_koch_segment(t, length, level-1)
        t.left(60)
        draw_koch_segment(t, length, level-1)
        t.right(120)
        draw_koch_segment(t, length, level-1)
        t.left(60)
        draw_koch_segment(t, length, level-1)

def draw_koch_snowflake(t, length, level):
    """Малює сніжинку Коха з трьох сегментів."""
    for _ in range(3):
        draw_koch_segment(t, length, level)
        t.right(120)

def main():
    # Введення рівня рекурсії від користувача
    level = int(input("Введіть рівень рекурсії для сніжинки Коха: "))
    
    # Налаштування Turtle
    t = turtle.Turtle()
    t.speed(0)  
    t.penup()
    t.goto(-150, 100)
    t.pendown()
    
    # Малюємо сніжинку Коха
    draw_koch_snowflake(t, 300, level)
    
    # Завершуємо малювання
    turtle.done()

if __name__ == "__main__":
    main()
