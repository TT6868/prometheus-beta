import time
from typing import Callable, Optional, List

class BrowserFrameRateLogger:
    """
    A class to log and track frame rates in a browser environment.
    
    This class provides methods to start, stop, and analyze frame rate performance.
    It can be used in both browser-side JavaScript and Python-based browser automation.
    """
    
    def __init__(self, sample_interval: float = 1.0):
        """
        Initialize the frame rate logger.
        
        :param sample_interval: Time interval for collecting frame rate samples (default: 1 second)
        """
        self.samples: List[float] = []
        self.start_time: Optional[float] = None
        self.sample_interval = sample_interval
        self.last_sample_time: Optional[float] = None
    
    def start(self) -> None:
        """
        Start frame rate logging.
        """
        self.samples.clear()
        self.start_time = time.time()
        self.last_sample_time = self.start_time
    
    def log_frame(self) -> None:
        """
        Log a frame in the current time collection.
        Call this method for each frame rendered.
        """
        current_time = time.time()
        
        # If no start time, implicitly start logging
        if self.start_time is None:
            self.start()
        
        # Check if we should take a sample
        if current_time - self.last_sample_time >= self.sample_interval:
            # Calculate frames per second for the interval
            frames_count = len(self.samples) + 1
            fps = frames_count / (current_time - self.last_sample_time)
            
            self.samples.append(fps)
            self.last_sample_time = current_time
    
    def stop(self) -> dict:
        """
        Stop frame rate logging and return performance metrics.
        
        :return: A dictionary containing frame rate performance metrics
        """
        if self.start_time is None:
            return {
                "error": "Logging was not started",
                "fps_samples": [],
                "avg_fps": 0,
                "min_fps": 0,
                "max_fps": 0,
                "total_duration": 0
            }
        
        # Add the last interval's frame rate if needed
        current_time = time.time()
        if self.last_sample_time and current_time - self.last_sample_time > 0:
            frames_count = len(self.samples) + 1
            fps = frames_count / (current_time - self.last_sample_time)
            self.samples.append(fps)
        
        total_duration = current_time - self.start_time
        
        # Reset logging state
        start_time, self.start_time = self.start_time, None
        
        return {
            "fps_samples": self.samples,
            "avg_fps": sum(self.samples) / len(self.samples) if self.samples else 0,
            "min_fps": min(self.samples) if self.samples else 0,
            "max_fps": max(self.samples) if self.samples else 0,
            "total_duration": total_duration
        }