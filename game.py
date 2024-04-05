import pygame
import sys

class Sphere:
    def __init__(self, x, y, radius, color):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.speed = 5
        self.direction = (0, 0)  # Dirección inicial

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.radius)

    def move(self):
        self.x += self.speed * self.direction[0]
        self.y += self.speed * self.direction[1]

        # Atravesar los bordes de la ventana
        if self.x <= -self.radius:
            self.x = WIDTH + self.radius
        elif self.x >= WIDTH + self.radius:
            self.x = -self.radius
        if self.y <= -self.radius:
            self.y = HEIGHT + self.radius
        elif self.y >= HEIGHT + self.radius:
            self.y = -self.radius

# Dimensiones de la ventana
WIDTH, HEIGHT = 800, 600

# Colores
WHITE = (255, 255, 255)

# Inicializar Pygame
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Esfera Moviendo con Atraviesa Bordes")

# Crear una esfera
sphere = Sphere(WIDTH // 2, HEIGHT // 2, 20, WHITE)

# Bucle principal
clock = pygame.time.Clock()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                sphere.direction = (0, -1)
            elif event.key == pygame.K_DOWN:
                sphere.direction = (0, 1)
            elif event.key == pygame.K_LEFT:
                sphere.direction = (-1, 0)
            elif event.key == pygame.K_RIGHT:
                sphere.direction = (1, 0)

    # Limpiar la pantalla
    screen.fill((0, 0, 0))

    # Mover y dibujar la esfera
    sphere.move()
    sphere.draw(screen)

    # Actualizar la pantalla
    pygame.display.flip()

    # Limitar la velocidad de fotogramas
    clock.tick(60)

