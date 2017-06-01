#pragma once

#ifdef WIN32
  #define SOCIAL_EXPORT __declspec(dllexport)
#else
  #define SOCIAL_EXPORT
#endif

SOCIAL_EXPORT void social();
