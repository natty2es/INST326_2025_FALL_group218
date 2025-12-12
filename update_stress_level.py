def update_stress_level(stress, sleep_hours, conflicts, chores_done):
    """
    Update the player's stress level for one day based on sleep, conflicts, and chores.

    Primary author: Nathaniel Mekonnen
    Technique claimed here:clamping + iteration over list

    Parameters:
        stress (int): Current stress level (0–100).
        sleep_hours (int): Hours of sleep (0–12).
        conflicts (list[int]): Conflict intensity values for the day.
        chores_done (bool): True if chores were completed, else False.

    Returns:
        int: Updated stress level (0–100).
    """


  
    if sleep_hours >= 8:
        stress -= 10
    elif sleep_hours >= 5:
        stress -= 5
    else:
        stress += 10

    for intensity in conflicts:
        stress += intensity

    if not chores_done:
        stress += 5

    stress = max(0, min(100, stress))

    return stress
