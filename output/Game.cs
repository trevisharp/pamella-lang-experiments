using System.Drawing;

using Pamella;
using Pamella.Views;

public class Game : View
{
    CustomState state;

    public Game(CustomState state)
    {
        this.state = state;
    }

    protected override void OnStart(IGraphics g)
    {
        Content = new View[]
        {
            new Counter(this.state)
        };
    }

    protected override void OnRender(IGraphics g)
    {
        state.x |= state.x + state.vx;
        state.y |= state.y + state.vy;

        if (state.x < 0 || state.x + 100 > g.Width) {
            state.vx |= -state.vx;
        }

        if (state.y < 0 || state.y + 100 > g.Height) {
            state.vy |= -state.vy;
        }
    }
}