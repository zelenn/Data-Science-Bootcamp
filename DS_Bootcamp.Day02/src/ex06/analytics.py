import os
from random import randint
import logging
import requests
import json
import config

class Research:
    def __init__(self, filepath):
        logging.info("Initializing Research with file: %s", filepath)
        if not os.path.exists(filepath):
            logging.error("File not found: %s", filepath)
            raise FileNotFoundError(f"File {filepath} not found.")
        self.filepath = filepath

    def file_reader(self, has_header=True):
        logging.info("Reading file: %s", self.filepath)
        with open(self.filepath, 'r') as f:
            lines = [line.strip() for line in f if line.strip()]
        data_lines = lines[1:] if has_header else lines
        data = []
        for line in data_lines:
            parts = line.split(',')
            if len(parts) != 2:
                logging.error("Invalid data line: %s", line)
                raise ValueError("Data line does not contain exactly two items.")
            try:
                row = [int(part) for part in parts]
            except Exception as e:
                logging.error("Error converting data to int: %s", e)
                raise ValueError("Data values must be integers.")
            if row[0] == row[1]:
                logging.error("Invalid row, both values same: %s", row)
                raise ValueError("Data row values must be one 0 and one 1.")
            data.append(row)
        logging.info("Finished reading file.")
        return data

    def send_telegram_message(self, message):
        logging.info("Sending Telegram message: %s", message)
        payload = {
            "chat_id": "_", # sorry censored
            "text": message
        }
        try:
            response = requests.post(config.TELEGRAM_WEBHOOK_URL, data=payload)
            if response.status_code == 200:
                logging.info("Telegram message sent successfully.")
            else:
                logging.error("Failed to send Telegram message, status code: %s", response.status_code)
        except Exception as e:
            logging.error("Exception sending Telegram message: %s", e)

class Calculations:
    def __init__(self, data):
        logging.info("Initializing Calculations.")
        self.data = data

    def counts(self):
        logging.info("Calculating counts.")
        head_count = 0
        tail_count = 0
        for row in self.data:
            if row[0] == 1:
                head_count += 1
            if row[1] == 1:
                tail_count += 1
        logging.info("Counts calculated: head=%d, tail=%d", head_count, tail_count)
        return head_count, tail_count

    def fractions(self, counts):
        logging.info("Calculating fractions from counts: %s", counts)
        head_count, tail_count = counts
        total = head_count + tail_count
        if total == 0:
            logging.warning("Total count is zero, returning zeros for fractions.")
            return 0, 0
        head_frac = (head_count / total) * 100
        tail_frac = (tail_count / total) * 100
        logging.info("Fractions calculated: head=%.2f, tail=%.2f", head_frac, tail_frac)
        return head_frac, tail_frac

class Analytics(Calculations):
    def __init__(self, data):
        logging.info("Initializing Analytics.")
        super().__init__(data)

    def predict_random(self, num_predictions):
        logging.info("Predicting random outcomes for %d predictions.", num_predictions)
        predictions = []
        for _ in range(num_predictions):
            head = randint(0, 1)
            tail = 1 - head
            predictions.append([head, tail])
        logging.info("Random predictions: %s", predictions)
        return predictions

    def predict_last(self):
        logging.info("Predicting last observation.")
        if not self.data:
            logging.warning("Data is empty, predict_last returning empty list.")
            return []
        last = self.data[-1]
        logging.info("Last observation: %s", last)
        return last

    def save_file(self, data, filename, extension):
        full_filename = f"{filename}.{extension}"
        logging.info("Saving data to file: %s", full_filename)
        try:
            with open(full_filename, 'w') as f:
                f.write(str(data))
            logging.info("Data saved successfully.")
        except Exception as e:
            logging.error("Error saving file: %s", e)
            raise e
