import re

def load_robot_data(file_path):
    with open(file_path) as file:
        lines = file.read().strip().splitlines()
    robots = []
    for line in lines:
        px, py, vx, vy = map(int, re.findall(r'-?\d+', line))
        robots.append((px, py, vx, vy))
    return robots

def calculate_safety_factor(robots, grid_width=101, grid_height=103, time_step=100):
    # Simulate robot positions after 'time_step' seconds
    for i in range(len(robots)):
        px, py, vx, vy = robots[i]
        px = (px + vx * time_step) % grid_width
        py = (py + vy * time_step) % grid_height
        robots[i] = (px, py, vx, vy)

    # Calculate quadrants
    mid_x, mid_y = grid_width // 2, grid_height // 2
    q1 = q2 = q3 = q4 = 0
    for px, py, _, _ in robots:
        if px < mid_x and py < mid_y:
            q1 += 1  # Top-left
        elif px > mid_x and py < mid_y:
            q2 += 1  # Top-right
        elif px < mid_x and py > mid_y:
            q3 += 1  # Bottom-left
        elif px > mid_x and py > mid_y:
            q4 += 1  # Bottom-right

    return q1 * q2 * q3 * q4

if __name__ == "__main__":
    file_path = "input.txt" 
    robots = load_robot_data(file_path)
    safety_factor = calculate_safety_factor(robots)
    print("Safety Factor:", safety_factor)