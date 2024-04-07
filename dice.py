import random
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

def roll_dice(dice_count, color):
    results = []
    for _ in range(dice_count):
        result = random.randint(1, 10)
        results.append(result)
        print(f"{color} dice roll: {result}")
    return results

def display_dice_images(black_results, red_results):
    total_results = black_results + red_results
    fig, axes = plt.subplots(1, len(total_results), figsize=(len(total_results) * 2, 2))
    fig.suptitle("Dice Rolls", fontsize=16)
    for i, result in enumerate(total_results):
        if i < len(black_results):
            color = "Black"
        else:
            color = "Red"
        img_path = f"img/{color.lower()}_dice_{result}.png"
        img = mpimg.imread(img_path)
        axes[i].imshow(img)
        axes[i].axis('off')
    plt.show()