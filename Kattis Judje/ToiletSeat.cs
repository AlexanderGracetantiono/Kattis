using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace toilet2_java
{
    class Program
    {
        static void Main(string[] args)
        {
            string masuk = Console.ReadLine();
            int pol1 = 0, pol2 = 0, pol3 = 0;

            for(int i = 1; i < masuk.Length; i++)
            {
                if (i == 1)
                {
                    if (masuk[0] == 'U' && masuk[1] == 'D') { pol1 += 2; }
                    if (masuk[0] == 'D') { pol1 += 1; }
                    if (masuk[0] == 'D' && masuk[1] == 'U') { pol2 += 2; }
                    if (masuk[0] == 'U') { pol2 += 1; }

                }
                else
                {
                    if (masuk[i] == 'D') { pol1 += 2; }
                    else if (masuk[i] == 'U') { pol2 += 2; }

                        
                }

                if (masuk[i - 1] != masuk[i]) { pol3 += 1; }
            }
            Console.Write(pol1 + "\n" + pol2 + "\n" + pol3);
            Console.ReadKey();
        }
    }
}
