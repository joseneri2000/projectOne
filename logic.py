import csv

class VoteLogic:
    def __init__(self):
        """
        Initializes the VoteLogic object
        Counters for both John and Jane
        Set for IDs that have voted
        """
        self.voted_ids = set()
        self.john_votes = 0
        self.jane_votes = 0

    def submit_vote(self, voter_id: str, candidate: str) -> tuple[str, str]:
        """
        Processes a vote submission.
        Arguments for the ID of the voter and the candidate the voter is voting for.
        Returns: A tuple containing the message (str) and the color (str) for displaying the result.
        """
        if not voter_id.isdigit() or len(voter_id) != 4:
            # If voter ID is not 4 digits, return error message in red
            return "ID must be 4 digits.", "red"

        if voter_id in self.voted_ids:
            # If voter ID has already voted, return error message in red
            return "This ID has already voted", "red"

        # Store the vote data in a CSV file
        try:
            with open("votes.csv", mode="a", newline="") as file:
                writer = csv.writer(file)
                writer.writerow([voter_id, candidate])
        except OSError as e:
            # Return error message in case of file I/O error
            return f"Error submitting vote: {e}", "red"

        self.voted_ids.add(voter_id)  # Add the voted ID to the set
        if candidate == "John":
            self.john_votes += 1  # Increase John's vote count
        else:
            self.jane_votes += 1  # Increase Jane's vote count

        # Return success message with candidate name in color black
        return f"Voted for {candidate}", "black"

    def get_total_votes(self) -> str:
        """
        Retrieves the total number of votes for each candidate.
        Returns: A formatted string containing the total votes for each candidate.
        """
        try:
            return f"Total Votes\nJohn: {self.john_votes}\nJane: {self.jane_votes}"
        except Exception as e:
            # Return error message in case of any exception during total votes retrieval
            return f"Error retrieving total votes: {e}"