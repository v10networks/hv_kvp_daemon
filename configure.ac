#                                               -*- Autoconf -*-
# Process this file with autoconf to produce a configure script.

AC_PREREQ([2.63])
AC_INIT(hv_userspace_daemon, 0.1, bugs@v10networks,ca)
AM_INIT_AUTOMAKE(hv_userspace_daemon, 0.1)
AC_OUTPUT(Makefile src/Makefile)

AC_CONFIG_SRCDIR([src/hv_kvp_daemon.c])
AC_CONFIG_HEADERS([config.h])
AC_PREFIX_DEFAULT(/usr)

# Checks for programs.
AC_PROG_CC

# Checks for libraries.

# Checks for header files.
AC_CHECK_HEADERS([arpa/inet.h fcntl.h mntent.h netdb.h stdlib.h string.h sys/ioctl.h sys/socket.h syslog.h unistd.h])
AC_CHECK_HEADER(linux/hyperv.h, ,[AC_MSG_RESULT(Using our copy of hyperv.h then)])

# Checks for typedefs, structures, and compiler characteristics.
AC_HEADER_STDBOOL
AC_C_INLINE
AC_TYPE_SIZE_T

# Checks for library functions.
AC_FUNC_GETMNTENT
AC_FUNC_MALLOC
AC_FUNC_REALLOC
AC_CHECK_FUNCS([gethostname getmntent memset mkdir socket strchr strdup strerror uname])

AC_OUTPUT
