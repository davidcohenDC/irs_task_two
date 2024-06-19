--- proximity.lua ---

local proximity = {}

local CLEAR_PATH_THRESHOLD = 0.3    -- Threshold for determining a clear path

--- Function to check if the path ahead is clear
function proximity.isPathClear(front_sensors)
    for _, i in ipairs(front_sensors) do
        if robot.proximity[i].value > CLEAR_PATH_THRESHOLD then
            return false
        end
    end
    return true
end

return proximity