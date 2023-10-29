
int merge(const List& m, const List& n, List& result)
{
    while (True)
    {
        if (m.cur != null and n.cur != null){
            if (m.cur <= n.cur)
            {
                result.add(m.cur);
                m.cur = m.next;
            }
            else
            {
                result.add(n.cur);
                n.cur = n.next;
            }
        }
        else if (m.cur == null and n.cur != null)
        {
            result.add(n.cur);
            n.cur = n.next;
        }
        else if (m.cur != null and n.cur == null)
        {
            result.add(m.cur);
            m.cur = m.next;
        }
        else
        {
            break;
        }
    }
    return 0;
}