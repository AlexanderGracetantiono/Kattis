using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace free_food
{
    class Program
    {
        static void Main(string[] args)
        {
            int cases = int.Parse(Console.ReadLine());
           
            string[] day_count=new string[365];
            int sum = 0;
            int x = 0;
            for(int n = 1; n <= cases; n++)
            {
                string[] day = Console.ReadLine().Split(' ');
                int day_s = int.Parse(day[0]);
                int day_t = int.Parse(day[1]);
                for(int c= day_s; c <= day_t; c++)
                {

                    for(int v = 0; v < 365; v++)
                    {
                        if (day_count[v] != null)
                        {
                            if (int.Parse(day_count[v]) == c)
                            {
                                //day_count[x] = c + "";
                              //   x++;
                                break;
                            }

                        }
                        else
                        {
                            day_count[x] = c + "";
                            x++;
                            break;
                        }
                    }
                   // x++;
                }
              
            
            }
            Console.WriteLine(x);
            Console.ReadKey();
        }
    }
}
