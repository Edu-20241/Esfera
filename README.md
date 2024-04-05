1. Le pedimos  a chat gpt lo siguiente : dame un código en el que una esfera se mueva en todasx la direcciones con lenguaje de orientacion a objetos.  Despues nos arrojo el siguiente código 
import pygame
import sys

class Sphere:
    def __init__(self, x, y, radius, color):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.speed_x = 1
        self.speed_y = 1

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.radius)

    def move(self):
        self.x += self.speed_x
        self.y += self.speed_y

        # Cambiar la dirección si alcanza los límites de la ventana
        if self.x <= 0 or self.x >= WIDTH:
            self.speed_x *= -1
        if self.y <= 0 or self.y >= HEIGHT:
            self.speed_y *= -1

# Dimensiones de la ventana
WIDTH, HEIGHT = 800, 600

# Colores
WHITE = (255, 255, 255)

# Inicializar Pygame
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Esfera Moviendo en Todas Direcciones")

# Crear una esfera
sphere = Sphere(WIDTH // 2, HEIGHT // 2, 20, WHITE)

# Bucle principal
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Limpiar la pantalla
    screen.fill((0, 0, 0))

    # Mover y dibujar la esfera
    sphere.move()
    sphere.draw(screen)

    # Actualizar la pantalla
    pygame.display.flip()

    # Pequeña pausa para controlar la velocidad de la animación
    pygame.time.delay(10)

- Despues le pedimos que la esfera se moviese en linea recta con el siguiente código que nos arrojo :
 import pygame
import sys

class Sphere:
    def __init__(self, x, y, radius, color):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.speed_x = 1
        self.speed_y = 1

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.radius)

    def move(self):
        self.x += self.speed_x
        self.y += self.speed_y

        # Cambiar la dirección si alcanza los límites de la ventana
        if self.x <= self.radius or self.x >= WIDTH - self.radius:
            self.speed_x *= -1
        if self.y <= self.radius or self.y >= HEIGHT - self.radius:
            self.speed_y *= -1

# Dimensiones de la ventana
WIDTH, HEIGHT = 800, 600

# Colores
WHITE = (255, 255, 255)

# Inicializar Pygame
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Esfera Moviendo en Todas Direcciones")

# Crear una esfera
sphere = Sphere(WIDTH // 2, HEIGHT // 2, 20, WHITE)

# Bucle principal
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Limpiar la pantalla
    screen.fill((0, 0, 0))

    # Mover y dibujar la esfera
    sphere.move()
    sphere.draw(screen)

    # Actualizar la pantalla
    pygame.display.flip()

    # Pequeña pausa para controlar la velocidad de la animación
    pygame.time.delay(10)

- Lastimosamente no se pudo ejecutar el código y le pedimos una variante :
  import pygame
import sys

class Sphere:
    def __init__(self, x, y, radius, color):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.speed_x = 2
        self.speed_y = 2

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.radius)

    def move(self):
        self.x += self.speed_x
        self.y += self.speed_y

        # Rebotar cuando alcanza los bordes de la ventana
        if self.x <= self.radius or self.x >= WIDTH - self.radius:
            self.speed_x *= -1
        if self.y <= self.radius or self.y >= HEIGHT - self.radius:
            self.speed_y *= -1

# Dimensiones de la ventana
WIDTH, HEIGHT = 800, 600

# Colores
WHITE = (255, 255, 255)

# Inicializar Pygame
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Esfera Moviendo en Todas Direcciones")

# Crear una esfera
sphere = Sphere(WIDTH // 2, HEIGHT // 2, 20, WHITE)

# Bucle principal
clock = pygame.time.Clock()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Limpiar la pantalla
    screen.fill((0, 0, 0))

    # Mover y dibujar la esfera
    sphere.move()
    sphere.draw(screen)

    # Actualizar la pantalla
    pygame.display.flip()

    # Limitar la velocidad de fotogramas
    clock.tick(60)

- le volvimos a pedir que la esfera se moviera en linea recta ya que no lo hacia , por eso nos arrojo el siguiente resultado:
 import pygame
import sys

class Sphere:
    def __init__(self, x, y, radius, color):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.speed = 5
        self.direction = (1, 0)  # Dirección inicial

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.radius)

    def move(self):
        self.x += self.speed * self.direction[0]
        self.y += self.speed * self.direction[1]

        # Rebotar cuando alcanza los bordes de la ventana
        if self.x <= self.radius or self.x >= WIDTH - self.radius:
            self.direction = (-self.direction[0], self.direction[1])
        if self.y <= self.radius or self.y >= HEIGHT - self.radius:
            self.direction = (self.direction[0], -self.direction[1])

# Dimensiones de la ventana
WIDTH, HEIGHT = 800, 600

# Colores
WHITE = (255, 255, 255)

# Inicializar Pygame
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Esfera Moviendo en Linea Recta")

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

- la esfera ya se movia de izquierda a derecha pero nop de arriba a abajo :
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

        # Rebotar cuando alcanza los bordes de la ventana
        if self.x <= self.radius or self.x >= WIDTH - self.radius:
            self.direction = (-self.direction[0], self.direction[1])
        if self.y <= self.radius or self.y >= HEIGHT - self.radius:
            self.direction = (self.direction[0], -self.direction[1])

# Dimensiones de la ventana
WIDTH, HEIGHT = 800, 600

# Colores
WHITE = (255, 255, 255)

# Inicializar Pygame
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Esfera Moviendo en Linea Recta")

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

- por último, necesitabamos que la esfera al llegar al limite de la ventana saliera por el lado opuesta en la dirección que fuera, y este es el código final :
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
