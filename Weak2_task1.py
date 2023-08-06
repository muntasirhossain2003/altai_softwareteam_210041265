def process_instructions(instructions, grid_size):
    rows, columns = grid_size
    x, y = 0, 0   # Rover's initial position
    direction = 'N'  # Rover's initial direction (North)

    # Helper function to update direction after turning left or right
    def update_direction(current_direction, turn):
        directions = ['N', 'E', 'S', 'W']
        current_index = directions.index(current_direction)
        if turn == 'L':
            return directions[(current_index - 1) % 4]
        elif turn == 'R':
            return directions[(current_index + 1) % 4]

    for instruction in instructions:
        if instruction == 'F':
            # Calculate the next position based on the current direction
            if direction == 'N':
                next_y = min(y + 1, rows - 1)
                if next_y != y:
                    y = next_y
            elif direction == 'E':
                next_x = min(x + 1, columns - 1)
                if next_x != x:
                    x = next_x
            elif direction == 'S':
                next_y = max(y - 1, 0)
                if next_y != y:
                    y = next_y
            elif direction == 'W':
                next_x = max(x - 1, 0)
                if next_x != x:
                    x = next_x
        elif instruction in ['L', 'R']:
            # Update the direction
            direction = update_direction(direction, instruction)

    return x, y, direction


