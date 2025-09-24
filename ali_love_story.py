import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np
from matplotlib.animation import FuncAnimation
import random

# Set up the figure and axis
fig, ax = plt.subplots(figsize=(12, 8))
ax.set_xlim(-10, 10)
ax.set_ylim(-8, 8)
ax.set_aspect('equal')
ax.axis('off')
ax.set_facecolor('lightblue')

# Character positions and states
ali_x, ali_y = -6, -2
girl_x, girl_y = 3, -2
flower_x, flower_y = None, None
show_flower = False
show_taking_flower = False
show_proposal = False
show_rejection = False
show_clouds = False
show_rain = False
rain_drops = []
frame_count = 0
ali_step_phase = 0
girl_step_phase = 0

# Animation phases
PHASE_WALKING = 0
PHASE_TAKING_FLOWER = 1
PHASE_PROPOSAL = 2
PHASE_REJECTION = 3
PHASE_GIRL_LEAVES = 4
PHASE_CLOUDS = 5
PHASE_RAIN = 6
PHASE_FLOWER_THROWN = 7
PHASE_ALI_LEAVES = 8

current_phase = PHASE_WALKING
phase_timer = 0

def draw_person(x, y, color='blue', direction=1, holding_flower=False, taking_flower=False, step_phase=0, is_girl=False):
    """Draw a simple stick figure person with walking animation and gender differences"""
    # Head
    head_size = 0.25 if is_girl else 0.3
    head = plt.Circle((x, y + 1.5), head_size, color=color, fill=True)
    ax.add_patch(head)
    
    # Hair for girl
    if is_girl:
        # Long hair
        hair_points = np.array([
            [x - 0.3, y + 1.7], [x - 0.2, y + 1.8], [x, y + 1.8], 
            [x + 0.2, y + 1.8], [x + 0.3, y + 1.7], [x + 0.25, y + 1.4],
            [x - 0.25, y + 1.4]
        ])
        hair_patch = patches.Polygon(hair_points, closed=True, color=color, alpha=0.7)
        ax.add_patch(hair_patch)
    
    # Body - complete torso for both
    if is_girl:
        # Girl's body (shorter)
        ax.plot([x, x], [y + 1.2, y + 0.4], color=color, linewidth=2)
        # Draw triangular dress/skirt
        dress_points = np.array([
            [x - 0.1, y + 0.4], [x + 0.1, y + 0.4],  # waist
            [x + 0.4, y - 0.2], [x - 0.4, y - 0.2]   # bottom of dress
        ])
        dress_patch = patches.Polygon(dress_points, closed=True, color=color, alpha=0.6)
        ax.add_patch(dress_patch)
    else:
        # Boy's complete body
        ax.plot([x, x], [y + 1.2, y - 0.5], color=color, linewidth=3)
    
    # Arms with hands
    arm_y_pos = y + 0.8 if is_girl else y + 0.5
    
    if taking_flower and not is_girl:
        # Right arm reaching into pocket (boy only)
        ax.plot([x, x + 0.4], [arm_y_pos, y - 0.3], color=color, linewidth=2)
        # Hand in pocket
        hand = plt.Circle((x + 0.4, y - 0.3), 0.05, color=color, fill=True)
        ax.add_patch(hand)
        # Left arm normal with hand
        ax.plot([x, x - 0.3], [arm_y_pos, y], color=color, linewidth=2)
        left_hand = plt.Circle((x - 0.3, y), 0.05, color=color, fill=True)
        ax.add_patch(left_hand)
    elif holding_flower and not is_girl:
        # Right arm extended holding flower - hand grabs the STEM (bottom part)
        ax.plot([x, x + 0.6], [arm_y_pos, y - 0.4], color=color, linewidth=2)
        # Hand holding the stem at the bottom
        hand = plt.Circle((x + 0.6, y - 0.4), 0.05, color=color, fill=True)
        ax.add_patch(hand)
        # Left arm normal with hand
        ax.plot([x, x - 0.3], [arm_y_pos, y], color=color, linewidth=2)
        left_hand = plt.Circle((x - 0.3, y), 0.05, color=color, fill=True)
        ax.add_patch(left_hand)
    else:
        # Normal arms with hands for both characters
        if direction != 0:
            arm_swing = 0.15 * np.sin(step_phase) if not is_girl else 0.1 * np.sin(step_phase)
        else:
            arm_swing = 0
        
        arm_offset = 0.3 * direction if direction != 0 else 0.3
        
        # Right arm and hand
        right_hand_x = x + arm_offset + arm_swing
        right_hand_y = y - arm_swing * 0.5
        ax.plot([x, right_hand_x], [arm_y_pos, right_hand_y], color=color, linewidth=2)
        right_hand = plt.Circle((right_hand_x, right_hand_y), 0.05, color=color, fill=True)
        ax.add_patch(right_hand)
        
        # Left arm and hand
        left_hand_x = x - arm_offset - arm_swing  
        left_hand_y = y + arm_swing * 0.5
        ax.plot([x, left_hand_x], [arm_y_pos, left_hand_y], color=color, linewidth=2)
        left_hand = plt.Circle((left_hand_x, left_hand_y), 0.05, color=color, fill=True)
        ax.add_patch(left_hand)
    
    # Legs with feet
    if is_girl:
        # Girl's legs (from under dress)
        leg_start_y = y - 0.2
        leg_length = 1.1
        if direction != 0 and not holding_flower and not taking_flower:
            # Walking legs for girl
            leg_swing = 0.2 * np.sin(step_phase)
            leg_lift = abs(0.08 * np.sin(step_phase))
            
            # Right leg and foot
            right_foot_x = x + 0.2 + leg_swing
            right_foot_y = leg_start_y - leg_length + leg_lift
            ax.plot([x, right_foot_x], [leg_start_y, right_foot_y], color=color, linewidth=2)
            right_foot = plt.Circle((right_foot_x, right_foot_y), 0.05, color=color, fill=True)
            ax.add_patch(right_foot)
            
            # Left leg and foot
            left_foot_x = x - 0.2 - leg_swing
            left_foot_y = leg_start_y - leg_length + leg_lift
            ax.plot([x, left_foot_x], [leg_start_y, left_foot_y], color=color, linewidth=2)
            left_foot = plt.Circle((left_foot_x, left_foot_y), 0.05, color=color, fill=True)
            ax.add_patch(left_foot)
        else:
            # Static legs for girl
            ax.plot([x, x + 0.2], [leg_start_y, leg_start_y - leg_length], color=color, linewidth=2)
            ax.plot([x, x - 0.2], [leg_start_y, leg_start_y - leg_length], color=color, linewidth=2)
            # Static feet
            right_foot = plt.Circle((x + 0.2, leg_start_y - leg_length), 0.05, color=color, fill=True)
            left_foot = plt.Circle((x - 0.2, leg_start_y - leg_length), 0.05, color=color, fill=True)
            ax.add_patch(right_foot)
            ax.add_patch(left_foot)
    else:
        # Boy's legs (normal)
        if direction != 0 and not holding_flower and not taking_flower:
            # Walking legs
            leg_swing = 0.25 * np.sin(step_phase)
            leg_lift = abs(0.1 * np.sin(step_phase))
            
            # Right leg and foot
            right_foot_x = x + 0.3 + leg_swing
            right_foot_y = y - 1.5 + leg_lift
            ax.plot([x, right_foot_x], [y - 0.5, right_foot_y], color=color, linewidth=2)
            right_foot = plt.Circle((right_foot_x, right_foot_y), 0.06, color=color, fill=True)
            ax.add_patch(right_foot)
            
            # Left leg and foot
            left_foot_x = x - 0.3 - leg_swing
            left_foot_y = y - 1.5 + leg_lift
            ax.plot([x, left_foot_x], [y - 0.5, left_foot_y], color=color, linewidth=2)
            left_foot = plt.Circle((left_foot_x, left_foot_y), 0.06, color=color, fill=True)
            ax.add_patch(left_foot)
        else:
            # Static legs
            ax.plot([x, x + 0.3], [y - 0.5, y - 1.5], color=color, linewidth=2)
            ax.plot([x, x - 0.3], [y - 0.5, y - 1.5], color=color, linewidth=2)
            # Static feet
            right_foot = plt.Circle((x + 0.3, y - 1.5), 0.06, color=color, fill=True)
            left_foot = plt.Circle((x - 0.3, y - 1.5), 0.06, color=color, fill=True)
            ax.add_patch(right_foot)
            ax.add_patch(left_foot)
    
    # Draw pocket outline when taking flower
    if taking_flower and not is_girl:
        pocket = patches.Rectangle((x + 0.1, y - 0.6), 0.4, 0.3, 
                                linewidth=1, edgecolor=color, facecolor='none', alpha=0.5)
        ax.add_patch(pocket)

def draw_flower(x, y, size=1):
    """Draw a flower with stem going down and flower head at top"""
    # Stem (green) - goes DOWN from the flower head
    stem_length = 0.8 * size
    ax.plot([x, x], [y, y - stem_length], color='green', linewidth=3)
    
    # Leaves on stem
    leaf_y = y - stem_length * 0.3
    ax.plot([x, x - 0.15], [leaf_y, leaf_y - 0.1], color='green', linewidth=2)
    ax.plot([x, x + 0.15], [leaf_y, leaf_y - 0.1], color='green', linewidth=2)
    
    # Flower head at TOP (at position x, y)
    petal_radius = 0.12 * size
    center_radius = 0.08 * size
    
    # Draw 5 petals around the flower head
    for i, angle in enumerate(np.linspace(0, 2*np.pi, 6)[:-1]):  # 5 petals
        petal_x = x + (center_radius + petal_radius * 0.7) * np.cos(angle)
        petal_y = y + (center_radius + petal_radius * 0.7) * np.sin(angle)
        petal = plt.Circle((petal_x, petal_y), petal_radius, color='red', fill=True, alpha=0.8)
        ax.add_patch(petal)
    
    # Flower center (yellow) at the TOP
    center = plt.Circle((x, y), center_radius, color='yellow', fill=True)
    ax.add_patch(center)
    
    # Small details in center
    for angle in np.linspace(0, 2*np.pi, 8):
        dot_x = x + 0.03 * np.cos(angle)
        dot_y = y + 0.03 * np.sin(angle)
        ax.plot(dot_x, dot_y, 'o', color='orange', markersize=1)

def draw_cloud(x, y, size=1):
    """Draw a simple cloud"""
    for i in range(3):
        cloud_x = x + (i - 1) * 0.5 * size
        cloud = plt.Circle((cloud_x, y), 0.4 * size, color='gray', fill=True, alpha=0.7)
        ax.add_patch(cloud)

def draw_rain_drop(x, y):
    """Draw a rain drop"""
    ax.plot([x, x], [y, y - 0.3], color='blue', linewidth=2, alpha=0.6)

def add_text(x, y, text, fontsize=10, color='black'):
    """Add text to the animation"""
    ax.text(x, y, text, fontsize=fontsize, ha='center', va='center', 
            bbox=dict(boxstyle="round,pad=0.3", facecolor="white", alpha=0.8),
            color=color)

def animate(frame):
    global ali_x, ali_y, girl_x, girl_y, flower_x, flower_y
    global show_flower, show_taking_flower, show_proposal, show_rejection, show_clouds, show_rain
    global current_phase, phase_timer, rain_drops, frame_count
    global ali_step_phase, girl_step_phase
    
    ax.clear()
    ax.set_xlim(-10, 10)
    ax.set_ylim(-8, 8)
    ax.set_aspect('equal')
    ax.axis('off')
    ax.set_facecolor('lightblue')
    
    frame_count += 1
    phase_timer += 1
    
    # Ground line
    ax.plot([-10, 10], [-3.5, -3.5], color='green', linewidth=5)
    
    # Phase management
    if current_phase == PHASE_WALKING:
        # Ali walks towards the girl
        if ali_x < 0:
            ali_x += 0.25  # Increased speed
            ali_step_phase += 0.5  # Walking animation
        else:
            current_phase = PHASE_TAKING_FLOWER
            phase_timer = 0
    
    elif current_phase == PHASE_TAKING_FLOWER:
        # Ali takes flower from his pocket
        show_taking_flower = True
        ali_step_phase = 0  # Stop walking animation
        if phase_timer > 15:  # Reduced from 30 to 15 frames
            show_taking_flower = False
            show_flower = True
            current_phase = PHASE_PROPOSAL
            phase_timer = 0
    
    elif current_phase == PHASE_PROPOSAL:
        # Ali proposes with flower - flower head positioned ABOVE his hand
        flower_x, flower_y = ali_x + 0.6, ali_y + 0.4  # Flower HEAD at top, stem goes down to his hand
        show_proposal = True
        if phase_timer > 25:  # Reduced from 45 to 25 frames
            current_phase = PHASE_REJECTION
            phase_timer = 0
    
    elif current_phase == PHASE_REJECTION:
        show_rejection = True
        show_proposal = False
        flower_x, flower_y = ali_x + 0.6, ali_y + 0.4  # Flower HEAD at top
        if phase_timer > 35:  # Reduced from 60 to 35 frames
            current_phase = PHASE_GIRL_LEAVES
            phase_timer = 0
    
    elif current_phase == PHASE_GIRL_LEAVES:
        # Girl walks away
        show_rejection = False
        flower_x, flower_y = ali_x + 0.6, ali_y + 0.4  # Flower HEAD at top
        if girl_x < 8:
            girl_x += 0.3  # Increased speed from 0.25 to 0.3
            girl_step_phase += 0.6  # Faster walking animation
        else:
            current_phase = PHASE_CLOUDS
            phase_timer = 0
    
    elif current_phase == PHASE_CLOUDS:
        show_clouds = True
        flower_x, flower_y = ali_x + 0.6, ali_y + 0.4  # Flower HEAD at top
        girl_step_phase = 0  # Stop walking animation
        if phase_timer > 20:  # Reduced from 45 to 20 frames
            current_phase = PHASE_RAIN
            phase_timer = 0
    
    elif current_phase == PHASE_RAIN:
        show_rain = True
        flower_x, flower_y = ali_x + 0.6, ali_y + 0.4  # Flower HEAD at top
        # Add new rain drops
        if frame_count % 2 == 0:  # More frequent rain
            for _ in range(6):
                rain_x = ali_x + random.uniform(-2, 2)
                rain_y = random.uniform(4, 7)
                rain_drops.append([rain_x, rain_y])
        
        # Update rain drops
        rain_drops = [[x, y - 0.4] for x, y in rain_drops if y > -3]  # Faster falling rain
        
        if phase_timer > 40:  # Reduced from 80 to 40 frames
            current_phase = PHASE_FLOWER_THROWN
            phase_timer = 0
    
    elif current_phase == PHASE_FLOWER_THROWN:
        # Ali throws flower away
        if show_flower and flower_x is not None:
            flower_x -= 0.5  # Faster throwing (increased from 0.4 to 0.5)
            flower_y -= 0.2  # Faster dropping (increased from 0.15 to 0.2)
            if flower_x < ali_x - 2:  # Reduced distance (from 2.5 to 2)
                show_flower = False
                current_phase = PHASE_ALI_LEAVES
                phase_timer = 0
    
    elif current_phase == PHASE_ALI_LEAVES:
        # Ali walks away sadly with clouds and rain following him
        if ali_x > -8:
            ali_x -= 0.15  # Increased speed
            ali_step_phase += 0.4  # Walking animation (slower/sadder)
            
            # Update rain drops to follow Ali as he moves
            if frame_count % 3 == 0:  # Continue adding rain that follows Ali
                for _ in range(4):
                    rain_x = ali_x + random.uniform(-1.5, 1.5)  # Rain follows Ali's position
                    rain_y = random.uniform(4, 6)
                    rain_drops.append([rain_x, rain_y])
            
            # Update existing rain drops
            rain_drops = [[x, y - 0.3] for x, y in rain_drops if y > -3]
    
    # Draw characters
    if current_phase <= PHASE_GIRL_LEAVES or current_phase == PHASE_ALI_LEAVES:
        if girl_x <= 7:  # Only draw girl if she hasn't left completely
            girl_direction = -1 if current_phase == PHASE_GIRL_LEAVES else 0
            draw_person(girl_x, girl_y, 'pink', girl_direction, False, False, girl_step_phase, True)
    
    # Draw Ali (different color when sad, holding flower when appropriate)
    ali_color = 'blue' if current_phase < PHASE_CLOUDS else 'darkblue'
    holding_flower = show_flower and current_phase >= PHASE_PROPOSAL and current_phase <= PHASE_RAIN
    ali_direction = 1 if current_phase == PHASE_WALKING else (-1 if current_phase == PHASE_ALI_LEAVES else 0)
    draw_person(ali_x, ali_y, ali_color, ali_direction, holding_flower, show_taking_flower, ali_step_phase, False)
    
    # Draw flower
    if show_flower and flower_x is not None:
        draw_flower(flower_x, flower_y)
    
    # Draw clouds
    if show_clouds or current_phase == PHASE_ALI_LEAVES:
        ax.set_facecolor('lightgray')
        # Clouds follow Ali's position
        cloud_center_x = ali_x if current_phase == PHASE_ALI_LEAVES else ali_x
        draw_cloud(cloud_center_x - 1, 5, 1.2)
        draw_cloud(cloud_center_x + 1, 4.5, 1)
        draw_cloud(cloud_center_x, 6, 1.5)
    
    # Draw rain
    if show_rain or current_phase == PHASE_ALI_LEAVES:
        ax.set_facecolor('gray')
        for rain_x, rain_y in rain_drops:
            draw_rain_drop(rain_x, rain_y)
    
    # Add dialogue
    if show_proposal:
        add_text(ali_x, ali_y + 3, "I Love you\nWill you marry me?", fontsize=12, color='blue')
    
    if show_rejection:
        add_text(girl_x, girl_y + 3, "I hate you!\nI love Haseeb.", fontsize=12, color='red')
    
    # Add title
    title_text = "Ali's Love Story"
    if current_phase >= PHASE_CLOUDS:
        title_text = "A Broken Heart"
    ax.text(0, 7, title_text, fontsize=16, ha='center', va='center', 
            bbox=dict(boxstyle="round,pad=0.5", facecolor="white", alpha=0.9),
            weight='bold')

# Create and run animation
anim = FuncAnimation(fig, animate, frames=600, interval=80, repeat=True)  # Faster animation
plt.tight_layout()
plt.show()

# To save as gif (uncomment the line below)
# anim.save('ali_love_story.gif', writer='pillow', fps=12)