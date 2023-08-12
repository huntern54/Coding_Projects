import tkinter as tk

def is_prime(n):
    # Check if n is a prime number
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def ulam_spiral(n, canvas):
    # Create a blank 2D list to hold the spiral
    spiral = [[0] * n for i in range(n)]

    # Set up variables to track the current position and direction
    x, y = n // 2, n // 2  # Start at the center of the spiral
    dx, dy = 0, -1  # Start moving upward

    # Calculate the position of the first dot in the GUI window
    xpos = canvas.winfo_width() // 2
    ypos = canvas.winfo_height() // 2

    # Iterate through the numbers in the spiral
    for i in range(1, n**2 + 1):
        # Mark the current position in the spiral
        spiral[x][y] = i
        # Calculate the next position
        if x + dx == n or y + dy == n or spiral[x + dx][y + dy]:
            # Change direction if the next position is outside the spiral or already marked
            dx, dy = -dy, dx
        x, y = x + dx, y + dy
        # Draw the number if it is prime
        if is_prime(i):
            # Calculate the position of the number in the GUI window
            xpos += 50 * dy
            ypos += 50 * dx
            # Draw the dot on the canvas
            canvas.create_oval(xpos - 5, ypos - 5, xpos + 5, ypos + 5, fill="black")
            # Connect the dot to the previous dot
            if i > 1:
                # Calculate the position of the previous dot
                prev_xpos = xpos - 50 * dy
                prev_ypos = ypos - 50 * dx
                # Draw the line
                canvas.create_line(prev_xpos, prev_ypos, xpos, ypos)


def main():
    # Set up the GUI window
    window = tk.Tk()
    window.title("Ulam Spiral")
    canvas = tk.Canvas(window, width=2000, height=2000, bg="white")
    canvas.pack()

    # Draw the Ulam spiral
    ulam_spiral(100, canvas)

    # Close the terminal when the window is closed
    window.protocol("WM_DELETE_WINDOW", window.destroy)

    # Run the GUI loop
    window.mainloop()


if __name__ == "__main__":
    main()
