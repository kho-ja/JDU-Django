"""
Custom Middleware for Django Project
"""

import time
import logging
from django.utils.deprecation import MiddlewareMixin

# Get logger instance
logger = logging.getLogger("request_logger")


class LogRequestTimeMiddleware(MiddlewareMixin):
    """
    Middleware that logs the request processing time to console.

    This middleware records when a request comes in and calculates
    how long it took to process the request and generate a response.
    """

    def process_request(self, request):
        """
        Called before Django decides which view to execute.
        Store the start time in the request object.
        """
        request.start_time = time.time()

        # Log request details
        print(f"\n{'=' * 60}")
        print(f"📥 INCOMING REQUEST")
        print(f"{'=' * 60}")
        print(f"⏰ Time: {time.strftime('%Y-%m-%d %H:%M:%S')}")
        print(f"🌐 Method: {request.method}")
        print(f"🔗 Path: {request.path}")
        print(f"👤 User: {request.user if hasattr(request, 'user') else 'Anonymous'}")
        print(f"{'=' * 60}\n")

    def process_response(self, request, response):
        """
        Called after the view has been executed.
        Calculate and log the processing time.
        """
        if hasattr(request, "start_time"):
            # Calculate processing time
            processing_time = time.time() - request.start_time

            # Log response details
            print(f"\n{'=' * 60}")
            print(f"📤 OUTGOING RESPONSE")
            print(f"{'=' * 60}")
            print(f"⏱️  Processing Time: {processing_time:.4f} seconds")
            print(f"📊 Status Code: {response.status_code}")
            print(f"🔗 Path: {request.path}")
            print(f"{'=' * 60}\n")

        return response


class RequestLoggingMiddleware(MiddlewareMixin):
    """
    Middleware that logs detailed information about each request to a file.

    This middleware logs:
    - Request method, path, and query parameters
    - User information
    - IP address
    - User agent
    - Response status code
    - Processing time
    """

    def process_request(self, request):
        """
        Log information when request comes in.
        """
        request.log_start_time = time.time()

        # Get client IP address
        x_forwarded_for = request.META.get("HTTP_X_FORWARDED_FOR")
        if x_forwarded_for:
            ip_address = x_forwarded_for.split(",")[0]
        else:
            ip_address = request.META.get("REMOTE_ADDR", "Unknown")

        # Get user agent
        user_agent = request.META.get("HTTP_USER_AGENT", "Unknown")

        # Store for use in response
        request.ip_address = ip_address
        request.user_agent = user_agent

        # Log request
        logger.info(
            f"REQUEST | "
            f"Method: {request.method} | "
            f"Path: {request.path} | "
            f"User: {request.user if hasattr(request, 'user') else 'Anonymous'} | "
            f"IP: {ip_address}"
        )

    def process_response(self, request, response):
        """
        Log information when response is generated.
        """
        if hasattr(request, "log_start_time"):
            processing_time = time.time() - request.log_start_time

            # Log response
            logger.info(
                f"RESPONSE | "
                f"Status: {response.status_code} | "
                f"Path: {request.path} | "
                f"Time: {processing_time:.4f}s | "
                f"User: {request.user if hasattr(request, 'user') else 'Anonymous'}"
            )

        return response

    def process_exception(self, request, exception):
        """
        Log when an exception occurs during request processing.
        """
        logger.error(
            f"EXCEPTION | "
            f"Path: {request.path} | "
            f"Error: {str(exception)} | "
            f"User: {request.user if hasattr(request, 'user') else 'Anonymous'}"
        )
        return None  # Continue with normal exception handling
