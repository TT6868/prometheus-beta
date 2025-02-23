import readline
import logging
from typing import Optional, Callable

class ReadlineLogger:
    """
    A utility class for logging interactive prompts using readline.
    
    This class provides methods to log user inputs captured through readline,
    with configurable logging levels and optional custom logging handlers.
    """
    
    def __init__(self, logger: Optional[logging.Logger] = None):
        """
        Initialize the ReadlineLogger.
        
        Args:
            logger (Optional[logging.Logger]): A custom logger. 
                If not provided, a default logger will be created.
        """
        # Use provided logger or create a default one
        self.logger = logger or logging.getLogger(__name__)
        
        # Store the original hook to restore it later if needed
        self._original_hook = readline.set_pre_input_hook(None)
    
    def log_prompt(self, 
                   prompt: str, 
                   log_level: int = logging.INFO, 
                   sanitize: bool = True) -> str:
        """
        Log an interactive prompt and capture user input.
        
        Args:
            prompt (str): The prompt to display to the user
            log_level (int): Logging level (default: logging.INFO)
            sanitize (bool): Whether to sanitize sensitive input (default: True)
        
        Returns:
            str: The user's input
        
        Raises:
            ValueError: If prompt is empty
        """
        # Validate input
        if not prompt:
            raise ValueError("Prompt cannot be empty")
        
        # Log the prompt
        self.logger.log(log_level, f"Prompt: {prompt}")
        
        # Capture input
        try:
            user_input = input(prompt)
            
            # Sanitize input if requested (replace with asterisks for sensitive info)
            logged_input = '*' * len(user_input) if sanitize else user_input
            
            # Log the input
            self.logger.log(log_level, f"Input received: {logged_input}")
            
            return user_input
        
        except (KeyboardInterrupt, EOFError) as e:
            # Log interruption
            self.logger.error(f"Input interrupted: {type(e).__name__}")
            raise
    
    def add_input_logging_hook(self, 
                                custom_hook: Optional[Callable] = None) -> None:
        """
        Add a custom pre-input logging hook.
        
        Args:
            custom_hook (Optional[Callable]): A custom function to be called 
                before input is read. If None, removes any existing hook.
        """
        def default_hook():
            """Default hook that logs when input is about to be read."""
            self.logger.debug("Preparing to read input")
        
        # Use custom hook or default hook
        hook = custom_hook if custom_hook is not None else default_hook
        
        # Set the hook
        readline.set_pre_input_hook(hook)
    
    def restore_original_hook(self) -> None:
        """
        Restore the original readline pre-input hook.
        """
        readline.set_pre_input_hook(self._original_hook)