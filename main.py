import pygame
from ball import Ball

pygame.init()

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREY = (45, 45, 45)

ARIAL = pygame.font.SysFont('arial', 60)

ARIAL_100 = pygame.font.SysFont('arial', 100)

WIDTH, HEIGHT = 900, 500
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pong")

FPS = 60
P_VEL = 8

ball = Ball(WHITE, 34, 34)
ball.rect.x = WIDTH//2 - ball.rect.width//2
ball.rect.y = HEIGHT//2 - ball.rect.height//2

sprites = pygame.sprite.Group()
sprites.add(ball)


def draw_screen(left, right, center, left_score, right_score):
    window.fill(BLACK)
    pygame.draw.rect(window, WHITE, left)
    pygame.draw.rect(window, WHITE, right)
    pygame.draw.rect(window, GREY, center)
    sprites.draw(window)

    left_score = ARIAL.render(str(left_score), 1, WHITE)
    right_score = ARIAL.render(str(right_score), 1, WHITE)
    window.blit(left_score, (WIDTH * 0.25, 15))
    window.blit(right_score, (WIDTH * 0.75, 15))

    pygame.display.update()


def handle_paddle_movement(left_paddle, right_paddle, keys_pressed):
    if keys_pressed[pygame.K_w] and left_paddle.y > 0:
        left_paddle.y -= P_VEL
    if keys_pressed[pygame.K_s] and left_paddle.y + left_paddle.height < HEIGHT:
        left_paddle.y += P_VEL
    if keys_pressed[pygame.K_UP] and right_paddle.y > 0:
        right_paddle.y -= P_VEL
    if keys_pressed[pygame.K_DOWN] and right_paddle.y + right_paddle.height < HEIGHT:
        right_paddle.y += P_VEL


def handle_ball_collision(left_score, right_score):
    if ball.rect.x + ball.rect.width >= WIDTH:
        left_score += 1
        ball.velocity[0] = -ball.velocity[0]
    if ball.rect.x <= 0:
        right_score += 1
        ball.velocity[0] = -ball.velocity[0]
    if ball.rect.y + ball.rect.height > HEIGHT:
        ball.velocity[1] = -ball.velocity[1]
    if ball.rect.y < 0:
        ball.velocity[1] = -ball.velocity[1]

    return left_score, right_score


def handle_paddle_collision(left_paddle, right_paddle):
    if ball.rect.x < left_paddle.x + left_paddle.width and ball.rect.y <= left_paddle.y + left_paddle.height and ball.rect.y >= left_paddle.y or ball.rect.x + ball.rect.width > right_paddle.x and ball.rect.y + ball.rect.height <= right_paddle.y + right_paddle.height and ball.rect.y + ball.rect.height >= right_paddle.y:
        ball.bounce()


def win(text):
    winner = ARIAL_100.render(text, 1, WHITE)
    window.blit(winner, (WIDTH//2 - winner.get_width() //
                2, HEIGHT//2 - winner.get_height() // 2))
    pygame.display.update()
    pygame.time.delay(5000)


def main():
    clock = pygame.time.Clock()

    left = pygame.Rect(20, 20, 10, 100)
    right = pygame.Rect(WIDTH - 10 - 20, HEIGHT - 75 - 20, 10, 100)
    center_line = pygame.Rect(WIDTH//2 - 4, 0, 8, HEIGHT)

    left_score, right_score = 0, 0

    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        sprites.update()
        left_score, right_score = handle_ball_collision(
            left_score, right_score)

        keys_pressed = pygame.key.get_pressed()
        handle_paddle_collision(left, right)
        handle_paddle_movement(left, right, keys_pressed)

        draw_screen(left, right, center_line, left_score, right_score)
        clock.tick(FPS)

        if left_score >= right_score and left_score == 10:
            win("Left player wins!")
            run = False
        elif left_score <= right_score and right_score == 10:
            win("Right player wins!")
            run = False
    main()


if __name__ == "__main__":
    main()
