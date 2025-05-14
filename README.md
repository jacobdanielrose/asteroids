# Asteroids Game 🚀

A Python-based clone of the classic Asteroids arcade game, built using object-oriented programming principles. Players control a spaceship, navigate through an asteroid field, and shoot to destroy asteroids while avoiding collisions.

> 🎮 **Built as part of the [Boot.dev](https://boot.dev) Backend Developer curriculum**, this project reinforces concepts in object-oriented design, collision detection, and game development.

---

## 🚀 Features

- **Spaceship Movement**: Rotate and thrust the ship using keyboard inputs.
- **Asteroid Field**: Navigate through randomly generated asteroids.
- **Shooting Mechanism**: Fire shots to destroy asteroids.
- **Collision Detection**: Detect and respond to collisions between the spaceship and asteroids.
- **Game Loop**: Continuous game loop with real-time updates.

---

## 📁 Project Structure
```
asteroids/
├── asteroid.py # Defines the Asteroid class
├── asteroidfield.py # Manages the asteroid field and game logic
├── circleshape.py # Utility for circular shapes and collision detection
├── constants.py # Stores constant values like screen dimensions
├── main.py # Entry point to start the game
├── player.py # Defines the Player class (spaceship)
├── requirements.txt # Python dependencies
└── shot.py # Defines the Shot class for projectiles
```
---

## 🛠️ Installation & Usage

### Prerequisites

- Python 3.x
- Pygame library

### Installation Steps

1. Clone the repository:
  ```bash
   git clone https://github.com/jacobdanielrose/asteroids.git
   cd asteroids
  ```

2. Install dependencies:
  ```bash
  pip install -r requirements.txt
  ```

4. Run the game:
  ```bash
  python main.py
  ```

---

## 🎮 Controls

- **Arrow Keys**: Rotate and thrust the spaceship.
- **Spacebar**: Fire shots.
- **Esc**: Exit the game.

---

## 📚 About

This project was created as part of the [Boot.dev](https://boot.dev) Backend Developer course. It serves as an introduction to game development using Python and Pygame, focusing on object-oriented design and real-time game mechanics.

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).
