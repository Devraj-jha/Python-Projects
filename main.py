import pygame
import pygame.locals
from OpenGL.GL import *
from OpenGL.GLU import *
import numpy as np
import math

class MazeGame3D:
    def __init__(self):
        # Initialize Pygame
        pygame.init()
        self.display_size = (800, 600)
        self.screen = pygame.display.set_mode(self.display_size, pygame.DOUBLEBUF | pygame.OPENGL)
        pygame.display.set_caption("3D Maze Explorer - Use WASD to move, Mouse to look around")
        
        # Set up OpenGL
        self.setup_opengl()
        
        # Game state
        self.running = True
        self.clock = pygame.time.Clock()
        
        # Player position and orientation
        self.player_pos = [1.5, 1.5]  # x, z coordinates (y is up)
        self.player_height = 0.5
        self.player_angle = 0  # Horizontal rotation
        self.player_vertical_angle = 0  # Vertical rotation
        self.movement_speed = 0.1
        self.rotation_speed = 0.002
        
        # Mouse control
        pygame.mouse.set_visible(False)
        pygame.event.set_grab(True)
        
        # Define the maze (1 = wall, 0 = path)
        self.maze = [
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 1, 1, 0, 1, 1, 1, 0, 1],
            [1, 0, 1, 0, 0, 0, 0, 1, 0, 1],
            [1, 0, 1, 0, 1, 1, 0, 1, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 1, 1, 1, 1, 1, 1, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 1, 0, 1, 0, 1, 1, 0, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
        ]
        
        # Colors
        self.floor_color = (0.3, 0.3, 0.3)
        self.wall_color = (0.2, 0.5, 0.8)
        self.ceiling_color = (0.1, 0.1, 0.2)
        
    def setup_opengl(self):
        """Initialize OpenGL settings"""
        glEnable(GL_DEPTH_TEST)
        glEnable(GL_LIGHTING)
        glEnable(GL_LIGHT0)
        
        # Set up lighting
        glLightfv(GL_LIGHT0, GL_POSITION, [2, 5, 2, 1])
        glLightfv(GL_LIGHT0, GL_AMBIENT, [0.2, 0.2, 0.2, 1])
        glLightfv(GL_LIGHT0, GL_DIFFUSE, [0.8, 0.8, 0.8, 1])
        
        glMatrixMode(GL_PROJECTION)
        gluPerspective(45, (self.display_size[0] / self.display_size[1]), 0.1, 50.0)
        glMatrixMode(GL_MODELVIEW)
        
    def handle_events(self):
        """Handle keyboard and mouse events"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.running = False
            elif event.type == pygame.MOUSEMOTION:
                # Mouse look
                dx, dy = event.rel
                self.player_angle -= dx * self.rotation_speed
                self.player_vertical_angle -= dy * self.rotation_speed
                # Limit vertical look
                self.player_vertical_angle = max(-math.pi/3, min(math.pi/3, self.player_vertical_angle))
        
        # Keyboard movement
        keys = pygame.key.get_pressed()
        move_x, move_z = 0, 0
        
        if keys[pygame.K_w]:  # Forward
            move_z -= self.movement_speed
        if keys[pygame.K_s]:  # Backward
            move_z += self.movement_speed
        if keys[pygame.K_a]:  # Left
            move_x -= self.movement_speed
        if keys[pygame.K_d]:  # Right
            move_x += self.movement_speed
        if keys[pygame.K_SPACE]:  # Up
            self.player_height += self.movement_speed
        if keys[pygame.K_LSHIFT]:  # Down
            self.player_height -= self.movement_speed
            
        # Limit player height
        self.player_height = max(0.2, min(2.0, self.player_height))
        
        # Apply movement with rotation
        new_x = self.player_pos[0] + move_x * math.cos(self.player_angle) + move_z * math.sin(self.player_angle)
        new_z = self.player_pos[1] + move_z * math.cos(self.player_angle) - move_x * math.sin(self.player_angle)
        
        # Collision detection
        if not self.is_wall(int(new_x), int(new_z)):
            self.player_pos[0] = new_x
            self.player_pos[1] = new_z
            
    def is_wall(self, x, z):
        """Check if a position is a wall"""
        if 0 <= x < len(self.maze[0]) and 0 <= z < len(self.maze):
            return self.maze[z][x] == 1
        return True  # Out of bounds counts as wall
        
    def draw_floor_and_ceiling(self):
        """Draw the floor and ceiling"""
        # Floor
        glColor3f(*self.floor_color)
        glBegin(GL_QUADS)
        glVertex3f(-1, 0, -1)
        glVertex3f(len(self.maze[0]) + 1, 0, -1)
        glVertex3f(len(self.maze[0]) + 1, 0, len(self.maze) + 1)
        glVertex3f(-1, 0, len(self.maze) + 1)
        glEnd()
        
        # Ceiling
        glColor3f(*self.ceiling_color)
        glBegin(GL_QUADS)
        glVertex3f(-1, 2, -1)
        glVertex3f(len(self.maze[0]) + 1, 2, -1)
        glVertex3f(len(self.maze[0]) + 1, 2, len(self.maze) + 1)
        glVertex3f(-1, 2, len(self.maze) + 1)
        glEnd()
        
    def draw_walls(self):
        """Draw the maze walls"""
        glColor3f(*self.wall_color)
        
        for z in range(len(self.maze)):
            for x in range(len(self.maze[0])):
                if self.maze[z][x] == 1:
                    # Draw a cube for each wall segment
                    glPushMatrix()
                    glTranslatef(x + 0.5, 1, z + 0.5)
                    self.draw_cube(0.5)
                    glPopMatrix()
                    
    def draw_cube(self, size):
        """Draw a cube of given size"""
        s = size
        
        # Front face
        glBegin(GL_QUADS)
        glVertex3f(-s, -s, -s)
        glVertex3f(s, -s, -s)
        glVertex3f(s, s, -s)
        glVertex3f(-s, s, -s)
        
        # Back face
        glVertex3f(-s, -s, s)
        glVertex3f(-s, s, s)
        glVertex3f(s, s, s)
        glVertex3f(s, -s, s)
        
        # Top face
        glVertex3f(-s, s, -s)
        glVertex3f(s, s, -s)
        glVertex3f(s, s, s)
        glVertex3f(-s, s, s)
        
        # Bottom face
        glVertex3f(-s, -s, -s)
        glVertex3f(-s, -s, s)
        glVertex3f(s, -s, s)
        glVertex3f(s, -s, -s)
        
        # Left face
        glVertex3f(-s, -s, -s)
        glVertex3f(-s, s, -s)
        glVertex3f(-s, s, s)
        glVertex3f(-s, -s, s)
        
        # Right face
        glVertex3f(s, -s, -s)
        glVertex3f(s, -s, s)
        glVertex3f(s, s, s)
        glVertex3f(s, s, -s)
        glEnd()
        
    def render(self):
        """Render the 3D scene"""
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glLoadIdentity()
        
        # Set camera position and orientation
        cam_x = self.player_pos[0]
        cam_y = self.player_height
        cam_z = self.player_pos[1]
        
        look_x = cam_x + math.sin(self.player_angle) * math.cos(self.player_vertical_angle)
        look_y = cam_y + math.sin(self.player_vertical_angle)
        look_z = cam_z + math.cos(self.player_angle) * math.cos(self.player_vertical_angle)
        
        gluLookAt(cam_x, cam_y, cam_z,  # Eye position
                  look_x, look_y, look_z,  # Look at point
                  0, 1, 0)  # Up vector
        
        # Draw the scene
        self.draw_floor_and_ceiling()
        self.draw_walls()
        
        pygame.display.flip()
        
    def run(self):
        """Main game loop"""
        while self.running:
            self.handle_events()
            self.render()
            self.clock.tick(60)
            
        pygame.quit()

if __name__ == "__main__":
    game = MazeGame3D()
    game.run()