#include <iostream>
#include "chat.h"
#include "social.h"

void social(){
    #ifdef NDEBUG
    std::cout << "Social Release!" <<std::endl;
    #else
    std::cout << "Social Debug!" <<std::endl;
    #endif
    chat();
}
