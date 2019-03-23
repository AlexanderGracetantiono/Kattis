using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Quality_lifeCalculator
{
    class Program
    {
        static void Main(string[] args)
        {
            int cases = int.Parse(Console.ReadLine());
            double sum = 0;
            for (int n = 1; n <= cases; n++)
            {
                string data = Console.ReadLine();
                string[] data_separate = data.Split(' ');
                double a = double.Parse( data_separate[0]);
                double b = double.Parse(data_separate[1]);
                
                sum += (a * b);

            }
            Console.WriteLine(sum);
            Console.ReadKey();
        }
    }
}
