import pytest
import time
from src.browser_framerate_logger import BrowserFrameRateLogger

def test_framerate_logger_basic_flow():
    """
    Test the basic flow of frame rate logging
    """
    logger = BrowserFrameRateLogger(sample_interval=0.1)
    logger.start()
    
    # Simulate frame rendering
    for _ in range(30):
        logger.log_frame()
        time.sleep(0.01)  # Simulate frame time
    
    result = logger.stop()
    
    assert "fps_samples" in result
    assert len(result["fps_samples"]) > 0
    assert result["avg_fps"] > 0
    assert result["min_fps"] > 0
    assert result["max_fps"] > 0
    assert result["total_duration"] > 0

def test_framerate_logger_no_start():
    """
    Test logging without explicitly starting
    """
    logger = BrowserFrameRateLogger()
    logger.log_frame()
    result = logger.stop()
    
    assert result["fps_samples"] is not None

def test_framerate_logger_stop_without_logging():
    """
    Test stopping logger without any logging
    """
    logger = BrowserFrameRateLogger()
    result = logger.stop()
    
    assert result["error"] is not None
    assert result["fps_samples"] == []
    assert result["avg_fps"] == 0

def test_framerate_logger_multiple_start_stop():
    """
    Test multiple start and stop cycles
    """
    logger = BrowserFrameRateLogger(sample_interval=0.1)
    
    # First cycle
    logger.start()
    for _ in range(20):
        logger.log_frame()
        time.sleep(0.01)
    result1 = logger.stop()
    
    # Second cycle
    logger.start()
    for _ in range(25):
        logger.log_frame()
        time.sleep(0.01)
    result2 = logger.stop()
    
    assert len(result1["fps_samples"]) > 0
    assert len(result2["fps_samples"]) > 0
    assert result1["avg_fps"] > 0
    assert result2["avg_fps"] > 0