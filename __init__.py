import sys
import logging
from logging import Logger
# from inspect import getframeinfo
import inspect
import sys, os, time, io, traceback, warnings, weakref, collections.abc


CRITICAL = logging.CRITICAL
FATAL = logging.FATAL
ERROR = logging.ERROR
WARNING = logging.WARNING
WARN = logging.WARN
INFO = logging.INFO
DEBUG = logging.DEBUG
NOTSET = logging.NOTSET


class XLogger(Logger):
    def __init__(self, name='xroot', level=logging.DEBUG):
        super().__init__(name, level)
        self.last_update = False

    def configure_format(self, apply2all=True, **kwargs):
        """
        Available options:
        name =True or False
        levelno =True or False
        levelname =True or False
        pathname =True or False
        filename =True or False
        module =True or False
        lineno =True or False
        funcName =True or False
        created =True or False
        asctime =True or False
        msecs =True or False
        relativeCreated =True or False
        thread =True or False
        threadName =True or False
        process =True or False
        message =True or False

        %(name)s            Name of the logger (logging channel)
        %(levelno)s         Numeric logging level for the message (DEBUG, INFO,
                            WARNING, ERROR, CRITICAL)
        %(levelname)s       Text logging level for the message ("DEBUG", "INFO",
                            "WARNING", "ERROR", "CRITICAL")
        %(pathname)s        Full pathname of the source file where the logging
                            call was issued (if available)
        %(filename)s        Filename portion of pathname
        %(module)s          Module (name portion of filename)
        %(lineno)d          Source line number where the logging call was issued
                            (if available)
        %(funcName)s        Function name
        %(created)f         Time when the LogRecord was created (time.time()
                            return value)
        %(asctime)s         Textual time when the LogRecord was created
        %(msecs)d           Millisecond portion of the creation time
        %(relativeCreated)d Time in milliseconds when the LogRecord was created,
                            relative to the time the logging module was loaded
                            (typically at application startup time)
        %(thread)d          Thread ID (if available)
        %(threadName)s      Thread name (if available)
        %(process)d         Process ID (if available)
        %(message)s         The result of record.getMessage(), computed just as
                            the record is emitted
        """

        name_formatter = "%(name)s" 
        levelno_formatter = "%(levelno)s" 
        levelname_formatter = "%(levelname)s" 
        pathname_formatter = "%(pathname)s" 
        filename_formatter = "%(filename)s" 
        module_formatter = "%(module)s" 
        lineno_formatter = "%(lineno)d" 
        funcName_formatter = "%(funcName)s" 
        created_formatter = "%(created)f" 
        asctime_formatter = "%(asctime)s" 
        msecs_formatter = "%(msecs)d" 
        relativeCreated_formatter = "%(relativeCreated)d" 
        thread_formatter = "%(thread)d" 
        threadName_formatter = "%(threadName)s" 
        process_formatter = "%(process)d" 
        message_formatter = "%(message)s" 

        fmt = ''
        if "name" in kwargs and kwargs["name"]:
            fmt += ":"+name_formatter

        if "levelno" in kwargs and kwargs["levelno"]:
            fmt += ":"+levelno_formatter

        if "levelname" in kwargs and kwargs["levelname"]:
            fmt += ":"+levelname_formatter

        if "pathname" in kwargs and kwargs["pathname"]:
            fmt += ":"+pathname_formatter

        if "filename" in kwargs and kwargs["filename"]:
            fmt += ":"+filename_formatter

        if "module" in kwargs and kwargs["module"]:
            fmt += ":"+module_formatter

        if "lineno" in kwargs and kwargs["lineno"]:
            fmt += ":"+lineno_formatter

        if "funcName" in kwargs and kwargs["funcName"]:
            fmt += ":"+funcName_formatter

        if "created" in kwargs and kwargs["created"]:
            fmt += ":"+created_formatter

        if "asctime" in kwargs and kwargs["asctime"]:
            fmt += ":"+asctime_formatter

        if "msecs" in kwargs and kwargs["msecs"]:
            fmt += ":"+msecs_formatter

        if "relativeCreated" in kwargs and kwargs["relativeCreated"]:
            fmt += ":"+relativeCreated_formatter

        if "thread" in kwargs and kwargs["thread"]:
            fmt += ":"+thread_formatter

        if "threadName" in kwargs and kwargs["threadName"]:
            fmt += ":"+threadName_formatter

        if "process" in kwargs and kwargs["process"]:
            fmt += ":"+process_formatter

        # if "message" in kwargs and kwargs["message"]:
        fmt += ":"+message_formatter

        fmt = fmt[1:]
        formatter = logging.Formatter(fmt)

        if apply2all:
            for h in self.handlers:
                h.setFormatter(formatter)

        return fmt

    # def findCaller(self, stack_info=False):
    #     """
    #     Find the stack frame of the caller so that we can note the source
    #     file name, line number and function name.
    #     """
    #     f = currentframe()
    #     #On some versions of IronPython, currentframe() returns None if
    #     #IronPython isn't run with -X:Frames.
    #     if f is not None:
    #         f = f.f_back
    #     rv = "(unknown file)", 0, "(unknown function)", None
    #     while hasattr(f, "f_code"):
    #         co = f.f_code
    #         filename = os.path.normcase(co.co_filename)
    #         if filename == logging._srcfile:
    #             f = f.f_back
    #             continue
    #         sinfo = None
    #         if stack_info:
    #             sio = io.StringIO()
    #             sio.write('Stack (most recent call last):\n')
    #             traceback.print_stack(f, file=sio)
    #             sinfo = sio.getvalue()
    #             if sinfo[-1] == '\n':
    #                 sinfo = sinfo[:-1]
    #             sio.close()
    #         rv = (co.co_filename, f.f_lineno, co.co_name, sinfo)
    #         break
    #     return rv



    def _xlog(self, level, msg):
        pass

    def debug(self, msg, *args, **kwargs):
        """
        Log 'msg % args' with severity 'DEBUG'.

        To pass exception information, use the keyword argument exc_info with
        a true value, e.g.

        xlogger.debug("Houston, we have a %s", "thorny problem", exc_info=1)
        """
        self.log(msg, *args, level=DEBUG, **kwargs)

    def info(self, msg, *args, **kwargs):
        """
        Log 'msg % args' with severity 'INFO'.

        To pass exception information, use the keyword argument exc_info with
        a true value, e.g.

        xlogger.info("Houston, we have a %s", "interesting problem", exc_info=1)
        """
        self.log(msg, *args, level=INFO, **kwargs)

    def warning(self, msg, *args, **kwargs):
        """
        Log 'msg % args' with severity 'WARNING'.

        To pass exception information, use the keyword argument exc_info with
        a true value, e.g.

        xlogger.warning("Houston, we have a %s", "bit of a problem", exc_info=1)
        """
        self.log(msg, *args, level=WARNING, **kwargs)

    def error(self, msg, *args, **kwargs):
        """
        Log 'msg % args' with severity 'ERROR'.

        To pass exception information, use the keyword argument exc_info with
        a true value, e.g.

        xlogger.error("Houston, we have a %s", "major problem", exc_info=1)
        """
        self.log(msg, *args, level=ERROR, **kwargs)
        

    def exception(self, msg, *args, exc_info=True, **kwargs):
        """
        Convenience method for logging an ERROR with exception information.
        """
        # self.error(msg, *args, exc_info=exc_info, **kwargs)
        self.error(msg, *args, exc_info=exc_info, **kwargs)

    def critical(self, msg, *args, **kwargs):
        """
        Log 'msg % args' with severity 'CRITICAL'.

        To pass exception information, use the keyword argument exc_info with
        a true value, e.g.

        xlogger.critical("Houston, we have a %s", "major disaster", exc_info=1)
        """
        self.log(msg, *args, level=CRITICAL, **kwargs)
        

    fatal = critical

    def log(self, msg, *args, level=INFO, update=False, **kwargs):
        # TODO handle level output and 
        if not self.isEnabledFor(level):
            return
        if msg is None:
            msg = ''

        # handle update
        if update:
            # updater start
            if not self.last_update:
                logging.StreamHandler.terminator = ""
                for h in self.handlers:
                    h.formatter._fmt = '\r' + h.formatter._fmt
                    h.formatter._style._fmt = '\r' + h.formatter._style._fmt                    
                    # print(h.formatter._fmt)

            self.last_update = True

        if not update and self.last_update:
            # update end
            self.last_update = False
            logging.StreamHandler.terminator = "\n"
            for h in self.handlers:
                h.formatter._fmt = h.formatter._fmt[1:]
                h.formatter._style._fmt = h.formatter._style._fmt[1:]
                # h.formatter = logging._defaultFormatter
            self.log('')
                
        # super().log(level, msg, *args, **kwargs)
        self._log(level, msg, args, **kwargs)

    def _log(self, level, msg, args, exc_info=None, extra=None, stack_info=False):
        """
        Low-level logging routine which creates a LogRecord and then calls
        all the handlers of this logger to handle the record.
        """
        sinfo = None
        if logging._srcfile:
            #IronPython doesn't track Python frames, so findCaller raises an
            #exception on some versions of IronPython. We trap it here so that
            #IronPython can use logging.
            try:
                fn, lno, func, sinfo = self.findCaller(stack_info)
            except ValueError: # pragma: no cover
                fn, lno, func = "(unknown file)", 0, "(unknown function)"
        else: # pragma: no cover
            fn, lno, func = "(unknown file)", 0, "(unknown function)"
        if exc_info:
            if isinstance(exc_info, BaseException):
                exc_info = (type(exc_info), exc_info, exc_info.__traceback__)
            elif not isinstance(exc_info, tuple):
                exc_info = sys.exc_info()
        record = self.makeRecord(self.name, level, fn, lno, msg, args,
                                 exc_info, func, extra, sinfo)
        self.handle(record)

    def fakemethod(self):
        return self.getcontextinfo()

    def getcontextinfo(self):
        '''
        return a frame info as a Traceback, e.g.:
        Traceback(filename='test.py', 
                    lineno=14, 
                    function='<module>', 
                    code_context=['cinfo = getcontextinfo()\n'], 
                    index=0)
        '''
        trace = inspect.getframeinfo(sys._getframe(1) if hasattr(sys, "_getframe") else None)
        info_dict = {
            'filename':trace.filename,
            'lineno':trace.lineno,
            'function':trace.function,
            'code_context':trace.code_context,
            'index':trace.index
        }
        return info_dict

    def __reduce__(self):
        return getLogger, ()


def getLogger(name=None):
    """
    Return a logger with the specified name, creating it if necessary.

    If no name is specified, return the root logger.
    """
    if name:
        return logging.Logger.manager.getLogger(name)
    else:
        return logging.root


def basicConfig(**kwargs):
    logging.basicConfig(**kwargs)

print('root', logging.root.handlers)

logging.root = XLogger(logging.NOTSET)
logging.Logger.root = logging.root
logging.Logger.manager = logging.Manager(logging.Logger.root)
basicConfig()

if hasattr(sys, '_getframe'):
    logging.currentframe = lambda: sys._getframe(3)
else: #pragma: no cover
    def currentframe():
        """Return the frame object for the caller's stack frame."""
        try:
            raise Exception
        except Exception:
            return sys.exc_info()[2].tb_frame.f_back

    logging.currentframe = currentframe

