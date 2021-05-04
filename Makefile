##
## EPITECH PROJECT, 2021
## Makefile
## File description:
## Makefile du 109titration
##

NAME	=	109titration

CP		=	cp

CHMOD	=	chmod

all :	$(NAME)

$(NAME) :
	$(CP) sources/main.py $(NAME)
	$(CHMOD) +x $(NAME)

clean :
	$(RM) $(NAME)

fclean :
	$(RM) $(NAME)

re :	fclean all

.PHONY :	all clean fclean re
