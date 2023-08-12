using System.Drawing;

using Pamella;
using Stately;

public class CounterState : State
{
    public Property<int> count;
    public Property<CustomState> sub;
    public Property<bool> clicked;

    public RectangleF area => new RectangleF(
        ((CustomState)sub).x, 
        ((CustomState)sub).y, 
        100, 100
    );
}

public class Counter : StateView<CounterState>
{
    CustomState state;

    public Counter(CustomState state)
    {
        this.state = state;
    }

    protected override void onStart(IGraphics g, CounterState stt)
    {
        stt.count |= 0;
        stt.sub |= this.state;
        stt.clicked |= false;
    }

    protected override void onRender(IGraphics g, CounterState stt)
    {
        g.Clear(Color.White);
        g.DrawText(stt.area, $"Clique em mim ({stt.count})");
    }

    protected override void onFrame(IGraphics g, CounterState stt)
    {
        if (!stt.clicked && stt.area.Contains(g.Cursor) && g.IsDown)
        {
            stt.clicked |= true;
        }
        else if (stt.clicked && stt.area.Contains(g.Cursor) && !g.IsDown)
        {
            stt.count |= stt.count + 1;
            stt.clicked |= false;
        }
        else if (stt.area.Contains(g.Cursor))
        {
            stt.clicked |= false;
        }
    }
}