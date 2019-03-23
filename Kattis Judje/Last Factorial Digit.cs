using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace lastdigit
{
    class Program
    { static int factor(int n)
        {
            if (n == 1) { return 1; }
            return factor(n - 1)*n;
        }
        static void Main(string[] args)
        {
            int cases = int.Parse(Console.ReadLine());
            for(int n = 1; n <= cases; n++)
            {
                int fak = int.Parse(Console.ReadLine());
                string hasil = factor(fak)+"";
                //int max = hasil.Length;
                Console.WriteLine(hasil[hasil.Length-1]);

            }
            Console.ReadKey();
        }
    }
}
