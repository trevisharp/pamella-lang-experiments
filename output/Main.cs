using Pamella;
using Stately;

public class CustomState : State
{
    public Property<float> x;
    public Property<float> y;
    public Property<float> vx;
    public Property<float> vy;
}

public class Main : View
{
    protected override void OnStart(IGraphics g)
    {
        CustomState state = new CustomState();
        state.x |= rand() * (g.Width - 100);
        state.y |= rand() * (g.Height - 100);
        state.vx |= choose(-5, 5);
        state.vy |= choose(-5, 5);

        Content = new View[] {
            new Game(state)
        };
    }

    public static float choose(float x, float y)
    {
        var value = System.Random.Shared.NextSingle();
        
        if (value < .5) {
            return x;
        }

        return y;
    }
}