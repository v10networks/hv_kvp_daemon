#                                               -*- Autoconf -*-
# Process this file with autoconf to produce a configure script.

AC_PREREQ([2.67])
AC_INIT(hv-kvp, git, [BUG-REPORT-ADDRESS])
AM_INIT_AUTOMAKE(hv-kvp, git)
AC_CONFIG_SRCDIR([hv_kvp_daemon.c])
AC_CONFIG_HEADERS([config.h])
AC_PREFIX_DEFAULT(/usr)
# Checks for programs.
AC_PROG_CC

# Checks for libraries.

# Checks for header files.
AC_CHECK_HEADERS([arpa/inet.h fcntl.h netdb.h stdlib.h string.h sys/socket.h syslog.h unistd.h])
AC_CHECK_HEADER(linux/hyperv.h, ,[AC_MSG_RESULT(Using our copy of hyperv.h then)])

# Checks for typedefs, structures, and compiler characteristics.
AC_HEADER_STDBOOL
AC_C_INLINE
AC_TYPE_SIZE_T

# Checks for library functions.
AC_FUNC_MALLOC
AC_FUNC_REALLOC
AC_CHECK_FUNCS([gethostname memset mkdir socket strchr strdup strerror uname])

AC_CONFIG_FILES([Makefile])
AC_OUTPUT

