using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace help_phd_out
{
    class Program
    {
        static void Main(string[] args)
        {
            int cases = int.Parse(Console.ReadLine());
            for (int n = 0; n < cases; n++)
            {
                string masukan = Console.ReadLine();
                if (masukan == "P=NP") { Console.WriteLine("skipped"); }
                else { string[] ooo = masukan.Split('+');
                    int a = int.Parse(ooo[0]);
                    int b = int.Parse(ooo[1]);
                    Console.WriteLine((a + b));
                }


            }
            Console.ReadKey();
        }
    }
}
