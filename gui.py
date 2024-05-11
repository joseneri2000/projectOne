from PyQt6.QtWidgets import QMainWindow, QLabel, QPushButton, QVBoxLayout, QWidget, QLineEdit, QRadioButton, QButtonGroup
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont
from logic import VoteLogic

class VoteGUI(QMainWindow):
    def __init__(self, logic: VoteLogic):
        super().__init__()
        self.logic = logic
        self.voted_ids = set()  # Set to store voted IDs
        self.initUI()

    # Creation of the main window
    def initUI(self) -> None:
        """
        Initializes the graphical user interface.
        """
        self.setWindowTitle("Voting")
        self.setGeometry(100, 100, 300, 400)

        # Container for organization
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        # Sets the layout to box
        layout = QVBoxLayout()
        central_widget.setLayout(layout)

        # creates the first header
        self.vote_header = QLabel("Voting Application")
        self.vote_header.setAlignment(Qt.AlignmentFlag.AlignCenter)
        font = QFont()
        font.setPointSize(15)
        self.vote_header.setFont(font)

        # Adds the layer
        layout.addWidget(self.vote_header)

        # ID input layout
        id_layout = QVBoxLayout()
        id_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addLayout(id_layout)

        # Label for amount of Digits
        id_label = QLabel("Four Digit ID:")
        id_layout.addWidget(id_label)

        # creates the input field
        self.id_input = QLineEdit()
        self.id_input.setMaximumWidth(100)  # Set maximum width for the QLineEdit widget
        id_layout.addWidget(self.id_input)

        # Second header above candidates
        self.second_header = QLabel("Candidates")
        self.second_header.setAlignment(Qt.AlignmentFlag.AlignCenter) # Moves to center
        font_2 = QFont()
        font_2.setPointSize(15)
        self.second_header.setFont(font_2)

        # Adds header to layout
        layout.addWidget(self.second_header)

        # Radio buttons for candidates
        candidates_layout = QVBoxLayout()
        candidates_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addLayout(candidates_layout)
        self.john_radio = QRadioButton("John")
        self.jane_radio = QRadioButton("Jane")

        # Group the radio buttons to ensure only one can be selected at a time
        self.button_group = QButtonGroup()
        self.button_group.addButton(self.john_radio)
        self.button_group.addButton(self.jane_radio)
        # Adds John and Jane widgets to layout
        candidates_layout.addWidget(self.john_radio)
        candidates_layout.addWidget(self.jane_radio)

        # Submit Vote button
        submit_button = QPushButton("Submit Vote")
        submit_button.clicked.connect(self.submit_vote)
        layout.addWidget(submit_button)
        self.total_button = QPushButton("Show Total Votes")
        self.total_button.clicked.connect(self.show_total_votes)
        layout.addWidget(self.total_button)

        # Button for exiting app
        self.exit_button = QPushButton("Exit")
        self.exit_button.clicked.connect(self.close)
        layout.addWidget(self.exit_button)

        # Label for displaying results
        self.results_label = QLabel("")
        layout.addWidget(self.results_label)

    def submit_vote(self) -> None:
        """
        Retrieve voter ID and their selected candidate from the Input fields. Uses submit_vote from logic
        model to process and updates the result label with its corresponding color and message
        """
        voter_id = self.id_input.text()
        candidate = "John" if self.john_radio.isChecked() else "Jane"
        message, color = self.logic.submit_vote(voter_id, candidate)
        self.update_results(message, color) # Updates the result label with message and color

    def show_total_votes(self) -> None:
        """
        Displays number of votes for both candidates by using get_total_votes from logic.
        """
        total_votes_message = self.logic.get_total_votes()
        self.update_results(total_votes_message, "black")  # Update results label with total votes message

    def update_results(self, message: str, color: str) -> None:
        """
        Updates results label with provided message and color
        """
        text_style = f"color: {color}"
        self.results_label.setStyleSheet(text_style)
        self.results_label.setText(message)