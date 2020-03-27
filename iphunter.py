# IP_Hunter by System Failure
# https://informaticayhacking.com
import json
import requests
import time
import os.path
import platform
import sys
from colorama import init, Fore, Back, Style
init()
rj = Fore.RED
vr = Fore.GREEN
ci = Fore.CYAN
az = Fore.BLUE
am = Fore.YELLOW
r = Style.RESET_ALL
sistema = platform.system()
linea = print(vr + '_______________________________________________' + r)
def proc():
    response = requests.get('http://ip-api.com/json/' + ip)
    jsonData = response.json()
    paquetes = json.dumps(jsonData, indent=2)
    f = open('ubicate.txt', 'w')
    f.write(paquetes)
    f.close
    with open('ubicate.txt', 'r') as f:
        reader = [linea.split() for linea in f]
        sta = reader[1]
        pais = reader[2]
        pa = reader[3]
        re = reader[4]
        reg = reader[5]
        ciudad = reader[6]
        zipc = reader[7]
        lat = reader[8]
        lon = reader[9]
        tmz = reader[10]
        isp = reader[11]
        az = reader[12]
        q = reader[14]
        
        lsta = ''.join(sta)
        lpais = ''.join(pais)
        lpa = ''.join(pa)
        lre = ''.join(re)
        lreg = ''.join(reg)
        lciudad = ''.join(ciudad)
        lzipc = ''.join(zipc)
        llat = ''.join(lat)
        llon = ''.join(lon)
        ltmz = ''.join(tmz)
        lisp = ''.join(isp)
        laz = ''.join(az)
        lq = ''.join(q)

        a = lsta[9:]
        status = ci + 'Estado: ' + r + a
        b = lpais[10:]
        Pais = ci + 'País: ' + r + b
        c = lpa[14:]
        codpa = ci + 'Código de país: ' + r  + c
        d = lre[9:]
        region = ci + 'C_Reg: ' + r  + d
        e = lreg[13:]
        Region = ci + 'Región: ' + r  + e
        f = lciudad[7:]
        ciudad = ci + 'Ciudad: ' + r  + f
        g = lzipc[6:]
        Zip = ci + 'Código Zip: ' + r  + g
        h = llat[6:]
        latitud = ci + 'Latitud: ' + r  + h
        i = llon[6:-1]
        longitud = ci + 'Longitud: ' + r  + i
        j = ltmz[11:]
        timezone = ci + 'Zona Horaria: ' + r  + j
        k = lisp[6:]
        isp = ci + 'ISP: ' + r  + k
        l = laz[6:]
        As = ci + 'Asociación: ' + r  + l
        m = lq[8:]
        query = ci + 'IP: ' + r  + m
        print(vr + '_______________________________________________\n' + r)
        print ('\n' + status + '\n')
        print(vr + '_______________________________________________\n' + r)
        print (Pais + '\n')
        print(vr + '_______________________________________________\n' + r)
        print (codpa + '\n')
        print(vr + '_______________________________________________\n' + r)
        print (region + '\n')
        print(vr + '_______________________________________________\n' + r)
        print (Region + '\n')
        print(vr + '_______________________________________________\n' + r)
        print (ciudad + '\n')
        print(vr + '_______________________________________________\n' + r)
        print (Zip + '\n')
        print(vr + '_______________________________________________\n' + r)
        print (latitud + '\n')
        print(vr + '_______________________________________________\n' + r)
        print (longitud + '\n')
        print(vr + '_______________________________________________\n' + r)
        print (timezone + '\n')
        print(vr + '_______________________________________________\n' + r)
        print (isp + '\n')
        print(vr + '_______________________________________________\n' + r)
        print (As + '\n')
        print(vr + '_______________________________________________\n' + r)
        print (query + '\n')
        print(vr + '_______________________________________________' + r)
        print (ci + '\nLink Google Maps: ' + r +'http://www.google.com/maps/place/{0}{1}'.format(h, i))
        print(vr + '_______________________________________________' + r)
        print (am + '_________ Informática y Hacking © 2020 ________')
        print(vr + '_______________________________________________' + r)

def banner():
    so()
    print (ci + '''\n                    `"-._                    
                      `. "-._                
                        T.   "-.             
                         $$p.   "-.          
                         $$$$b.    `,        
                      .g$$$$$$$b    ;        
                    .d$$$$$$$$$$;   ;        
                 __d$$$$$$P""^T$$   :        
               .d$$$$P^^""___       :        
              d$P'__..gg$$$$$$$$$$; ;        
             d$$ :$$$$$$$$$$$$$$$$;  ;       
            :$$; $$$$$$$$$$$$$$$$P  :$       
            $$$  $$$$$$$$$$$$$$$$b  $$       
           :$$$ :$$$$$$$$$$$$$$$$$; $$;      
           $$$; $$$$$$$$$$$$$$$$$$; $$;      
          :$$$  $$$$$$$$$^$$$$$$$$$ :$$      
          $$$; :$$$p__gP' `Tp__g$$$ :$$      
         :$$$  $$P`T$P' .$. `T$P'T$; $$;     
         $$$; :$$;     :P^T;     :$; $$;     
        :$$$  $$$$-.           .-$$$ :$$     
        $$$$ :$$$$; \   T$P   / :$$$  $$     
       :$$$; $$$$$$  ; b:$;d :  $$$$; $$;    
       $$$$; $$$$$$; : T T T ; :$$$$$ :$$    
    .g$$$$$  :$$$$$$  ;' | ':  $$$$$$  T$b   
 .g$$$$$$$$   $$$$$$b :     ; d$$$$$;   `Tb  
:$$$$$$$$$;   :$$$$$$$;     :$$$$$$P       \ 
:$$$$$$$$$;    T$$$$$$$p._.g$$$$$$P         ;
$$$P^^T$$$$p.   `T$$$$$$$$$$$$$$P'     _/`. :
       `T$$$$$b.  `T$$$$$$$$$$P'    .g$P   \;
System Failure $b.  "^T$$$$P^"     d$P'      
           `T$$$$$b.             .dP'        
             "^T$$$$b.        .g$P'          
                "^T$$$b    .g$P^"            
                   "^T$b.g$P^"               
                      "^$^"                  
''' + r + az + '''_______________________________________________
_____________''' + r + '''Informática y Hacking''' + az + '''_____________
_______________________________________________
________''' + r + '''https://informaticayhacking.com''' + az + '''________
_______________________________________________
________________''' + r + rj + Style.BRIGHT + '''I P  H U N T E R''' + r + az + '''_______________\n''' + r)


def so():
    if sistema == 'Windows':
        os.system('cls')
    elif sistema == 'Linux':
        os.system('clear')
    else:
        banner()
        print (rj + 'Sistema operativo no reconocido.' + r)
banner()
print ('\n' + vr + '[' + r + '-' + vr + ']' + r + am + ' Ingrese una dirección IP o Dominio para ubicar:\n' + r)
ip = input(ci + ' >>  ' + r)
time.sleep(2)
if len(ip) > 0:
    so()
    banner()
    proc()
elif len(ip) == 0:
    print ('\n' + ci + 'Se tomará tu IP por defecto.' + r)
    so()
    banner()
    proc()
# Informática y Hacking © 2020
