import pygame
import random


def generate_mole_position(screen_width, screen_height, grid_size, mole_size):
    grid_x = random.randint(0, (screen_width // grid_size) - 1) * grid_size
    grid_y = random.randint(0, (screen_height // grid_size) - 1) * grid_size
    return (grid_x + (grid_size - mole_size) // 2, grid_y + (grid_size - mole_size) // 2)


def main():
    try:
        pygame.init()
        screen_width = 640
        screen_height = 512
        grid_size = 64
        mole_size = 64
        mole_image_path = "mole.png"

        mole_image = pygame.image.load(mole_image_path)
        mole_image = pygame.transform.scale(mole_image, (mole_size, mole_size))
        screen = pygame.display.set_mode((screen_width, screen_height))

        mole_pos = generate_mole_position(screen_width, screen_height, grid_size, mole_size)
        mole_rect = pygame.Rect(mole_pos[0], mole_pos[1], mole_size, mole_size)

        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if mole_rect.collidepoint(event.pos):

                        mole_pos = generate_mole_position(screen_width, screen_height, grid_size, mole_size)
                        mole_rect.topleft = mole_pos

            screen.fill((181,183,35))
            for x in range(0, screen_width, grid_size):
                pygame.draw.line(screen, "blue", (x, 0), (x, screen_height))
            for y in range(0, screen_height, grid_size):
                pygame.draw.line(screen, "blue", (0, y), (screen_width, y))


            screen.blit(mole_image, mole_pos)

            pygame.display.flip()
    finally:
        pygame.quit()
        #githubtest

if __name__ == "__main__":
    main()