using System.Collections.Generic;
using System.IO;
using System.Linq;

using Newtonsoft.Json;

public class ColorConverter
{
    public List<Color> AvailableColors;

    public ColorConverter()
    {
        const string FilePath = @"../../../colors.json";
        var json = File.ReadAllText(FilePath);
        var list = JsonConvert.DeserializeObject<List<Color>>(json);
        AvailableColors = list;
    }

    public Color GetColorByName(string colorName)
    {
        return AvailableColors.FirstOrDefault(c => c.Name == colorName);
    }
}

public class Color
{
    [JsonProperty("name")]
    public string Name;

    [JsonProperty("hue")]
    public int Hue;

    [JsonProperty("sat")]
    public int Sat;

    [JsonProperty("bri")]
    public int Bri;
}