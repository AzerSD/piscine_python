# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    format_ft_time.py                                  :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: asioud <asioud@student.42.fr>              +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2023/10/15 04:28:09 by asioud            #+#    #+#              #
#    Updated: 2023/10/15 04:55:29 by asioud           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import datetime as date
import time as time

print("Seconds passed since January 1, 1970: {date} or {sdate:.2e} in scientific notation"
    .format(date=time.time(), sdate=time.time()))

print(date.date.today().strftime("%b %d %Y"))
