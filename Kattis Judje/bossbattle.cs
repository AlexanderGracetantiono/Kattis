using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace boss_battle
{
    class Program
    {
        static void Main(string[] args)
        {
            int pillar = int.Parse(Console.ReadLine());
            int bomb = pillar - 2;
            if (bomb<=0) { bomb = 1; }
            Console.WriteLine(bomb);
            Console.ReadKey();
        }
    }
}
